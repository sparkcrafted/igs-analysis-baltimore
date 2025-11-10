import geopandas as gpd
import awswrangler as wr
import pandas as pd
from pathlib import Path
from config import PROJ_SHAPES, S3_CLEAN, S3_CURATED

CLEAN = S3_CLEAN
CURATED = S3_CURATED


# 1. Load tracts from your local standardized file
tracts_fp = PROJ_SHAPES / "baltimore_tracts_2020.geojson"
tracts = gpd.read_file(tracts_fp)[["tract_id", "geometry"]]
print(f"Loaded {len(tracts)} tracts")

# 2. Load school counts (from S3 clean zone)
sch_counts = wr.s3.read_parquet(f"{CLEAN}/features/tract_schools_count/")
print(f"Loaded {len(sch_counts)} school count records")

# 3. Join and aggregate (add placeholders for future features)
curated = (
    tracts.merge(sch_counts, on="tract_id", how="left")
    .fillna({"schools_count": 0, "points_count": 0})
    .rename(columns={"points_count": "schools_count"})
)

# ---- NEW: make it Athena-friendly (no Shapely geometry) ----
df_out = curated.drop(columns=["geometry"]).copy()
df_out["tract_id"] = df_out["tract_id"].astype(str)  # explicit type

# 4. Write Parquet to curated zone
wr.s3.to_parquet(
    df=df_out,
    path=f"{CURATED}/tract_features/",
    dataset=True,
    index=False,
    mode="overwrite",
)
print(f"Saved curated dataset to {CURATED}/tract_features/")
