import re
import numpy as np
import pandas as pd
import geopandas as gpd
import awswrangler as wr
from config import PROJ_SHAPES, S3_CLEAN, S3_CURATED

FEATURES_ROOT = f"{S3_CLEAN}/features/"

# ---- helpers ---------------------------------------------------------------

def list_feature_dirs(root: str) -> list[str]:
    """Return clean/features/*/ directories on S3 (no trailing slash in names)."""
    dirs = wr.s3.list_directories(root)  # returns e.g. ['s3://.../features/tract_schools_count/']
    out = []
    for d in dirs:
        # keep leaf name (e.g., 'tract_schools_count')
        leaf = d.rstrip("/").split("/")[-1]
        out.append((leaf, d.rstrip("/")))
    return out

ID_LIKE = {"tractid", "tract_id", "geoid", "geoid10", "geoid20", "name", "objectid"}
NON_VALUE_HINTS = {"shape_area", "shape_length", "geometry"}

def pick_value_column(df: pd.DataFrame) -> str:
    """
    Choose the most likely numeric value column to use as the feature value.
    Heuristics:
      1) prefer columns ending with known tokens: count, rate, score, index, value
      2) else first numeric column not in id/geometry-ish set
    """
    cols = list(df.columns)

    # normalize
    lowered = {c: c.lower() for c in cols}

    # candidates by name
    priority_regex = re.compile(r"(count|rate|score|index|value)$", re.I)
    for c in cols:
        cl = lowered[c]
        if c != "geometry" and priority_regex.search(cl):
            # make sure it's numeric
            s = pd.to_numeric(df[c], errors="coerce")
            if s.notna().any():
                return c

    # generic first numeric (excluding ids / geometry-ish)
    for c in cols:
        cl = lowered[c]
        if cl in ID_LIKE or cl in NON_VALUE_HINTS:
            continue
        s = pd.to_numeric(df[c], errors="coerce")
        if s.notna().any():
            return c

    # last resort: raise
    raise ValueError("Could not pick a numeric value column from: " + ", ".join(cols))

def normalize_id_column(df: pd.DataFrame) -> pd.DataFrame:
    """Return df with a 'tract_id' column (string) if possible."""
    for k in ["tract_id", "TRACT_ID", "GEOID", "GEOID20", "GEOID10", "tractid"]:
        if k in df.columns:
            out = df.rename(columns={k: "tract_id"}).copy()
            out["tract_id"] = out["tract_id"].astype(str).str.strip()
            return out
    # try to detect any id-like column
    for c in df.columns:
        if c.lower() in ID_LIKE:
            out = df.rename(columns={c: "tract_id"}).copy()
            out["tract_id"] = out["tract_id"].astype(str).str.strip()
            return out
    raise ValueError("No tract id column found in feature DataFrame.")

# ---- main -----------------------------------------------------------------

print("Listing feature directories under:", FEATURES_ROOT)
feature_dirs = list_feature_dirs(FEATURES_ROOT)
if not feature_dirs:
    raise SystemExit("No feature directories found. Upload features to clean/features/*/ first.")

print("Found features:", [name for name,_ in feature_dirs])

# base: all tracts (for full outer-coverage of Baltimore)
tracts = gpd.read_file(PROJ_SHAPES / "baltimore_tracts_2020.geojson")[["tract_id", "geometry"]]
base = pd.DataFrame({"tract_id": tracts["tract_id"].astype(str)})

merged = base.copy()

summary = []
for feat_name, feat_path in feature_dirs:
    try:
        df = wr.s3.read_parquet(f"{feat_path}/")
    except Exception as e:
        print(f"!! Skipping {feat_name}: failed to read parquet: {e}")
        continue

    # normalize id
    try:
        df = normalize_id_column(df)
    except Exception as e:
        print(f"!! Skipping {feat_name}: {e}")
        continue

    # drop geometry if present
    if "geometry" in df.columns:
        df = df.drop(columns=["geometry"])

    # pick value column
    try:
        val_col = pick_value_column(df)
    except Exception as e:
        print(f"!! Skipping {feat_name}: {e}")
        continue

    # coerce numeric
    df[val_col] = pd.to_numeric(df[val_col], errors="coerce")

    # keep just id + value, rename to feature key
    out_col = feat_name  # column name equals folder name
    df_small = df[["tract_id", val_col]].rename(columns={val_col: out_col})

    before = len(merged)
    merged = merged.merge(df_small, on="tract_id", how="left")
    after = len(merged)
    summary.append((feat_name, val_col, out_col, before, after, df_small[out_col].notna().sum()))
    print(f"✓ Merged feature '{feat_name}' (picked '{val_col}') -> column '{out_col}'. Coverage non-null rows={df_small[out_col].notna().sum()}")

# fill NaNs in obvious count-like columns with 0
for c in merged.columns:
    if c == "tract_id":
        continue
    if re.search(r"(count|total|num|n)$", c, re.I):
        merged[c] = merged[c].fillna(0).astype(float)

# write curated (no geometry)
wr.s3.to_parquet(
    df=merged,
    path=f"{S3_CURATED}/tract_features/",
    dataset=True,
    index=False,
    mode="overwrite",
)
print(f"Saved curated dynamic dataset to {S3_CURATED}/tract_features/")
print("Feature merge summary:")
for row in summary:
    print("  - name=", row[0], " picked=", row[1], " as=", row[2], " rows(before/after)=", row[3], "/", row[4], " nonnull=", row[5])
