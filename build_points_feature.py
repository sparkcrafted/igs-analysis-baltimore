import sys
import json
import pandas as pd
import geopandas as gpd
import awswrangler as wr
from pathlib import Path
from typing import Optional
from config import PROJ_SHAPES, S3_CLEAN

USUAL_LON_KEYS = ["lon","lng","longitude","x"]
USUAL_LAT_KEYS = ["lat","latitude","y"]

def load_points_any(path: str, lon_col: Optional[str]=None, lat_col: Optional[str]=None) -> gpd.GeoDataFrame:
    """
    Load points from local path or s3://...; supports:
      - CSV (needs lon/lat columns; auto-detect if not given)
      - GeoJSON / Shapefile / GeoPackage (any GeoPandas-readable)
    Returns EPSG:4326 by default and reprojects to tracts later.
    """
    p = str(path)
    # CSV
    if p.lower().endswith(".csv"):
        df = wr.s3.read_csv(p) if p.startswith("s3://") else pd.read_csv(p)
        if lon_col is None:
            for k in USUAL_LON_KEYS:
                if k in df.columns: lon_col = k; break
        if lat_col is None:
            for k in USUAL_LAT_KEYS:
                if k in df.columns: lat_col = k; break
        if not lon_col or not lat_col:
            raise ValueError("Could not find lon/lat columns. Provide --lon --lat.")
        gdf = gpd.GeoDataFrame(
            df,
            geometry=gpd.points_from_xy(df[lon_col], df[lat_col]),
            crs="EPSG:4326"
        )
        return gdf

    # Everything else (GeoJSON/Shapefile/GeoPackage/Parquet with geometry)
    gdf = gpd.read_file(p) if not p.startswith("s3://") else gpd.read_file(p)
    if gdf.crs is None:
        gdf = gdf.set_crs(4326)
    return gdf

def build_feature(points_path: str, feature_key: str, lon: Optional[str]=None, lat: Optional[str]=None):
    """
    feature_key will name the column + folder, e.g. banks -> tract_banks_count/.
    """
    # load base tracts
    tracts = gpd.read_file(PROJ_SHAPES / "baltimore_tracts_2020.geojson")[["tract_id","geometry"]]
    # load points
    pts = load_points_any(points_path, lon_col=lon, lat_col=lat)
    # align CRS
    pts = pts.to_crs(tracts.crs)

    # spatial join + count
    joined = gpd.sjoin(pts[["geometry"]], tracts, how="left", predicate="within")
    counts = (
        joined.groupby("tract_id", dropna=False).size()
        .rename(f"{feature_key}_count")
        .reset_index()
    )
    # write to S3 (clean/features/tract_<feature_key>_count/)
    dest = f"{S3_CLEAN}/features/tract_{feature_key}_count/"
    wr.s3.to_parquet(counts, path=dest, dataset=True, index=False, mode="overwrite")
    print("Wrote feature to:", dest)

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Build tract-level counts from point data")
    ap.add_argument("--path", required=True, help="Local or s3 path to points (CSV/GeoJSON/...)")
    ap.add_argument("--feature", required=True, help="feature key, e.g. banks, clinics")
    ap.add_argument("--lon", help="lon column for CSV")
    ap.add_argument("--lat", help="lat column for CSV")
    args = ap.parse_args()
    build_feature(args.path, args.feature, lon=args.lon, lat=args.lat)
