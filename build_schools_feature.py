import geopandas as gpd
import pandas as pd
import awswrangler as wr
from config import PROJ_SHAPES, RAW_SHAPES, S3_CLEAN

# Load tracts (standardized file you already created)
tracts = gpd.read_file(PROJ_SHAPES / "baltimore_tracts_2020.geojson")[["tract_id","geometry"]]

# Load schools (GeoJSON in data_raw/shapes)
schools = gpd.read_file(RAW_SHAPES / "Baltimore_City_Schools.geojson")

# Ensure CRS compatibility
if schools.crs is None:
    schools.set_crs(epsg=4326, inplace=True)
schools = schools.to_crs(tracts.crs)

# Spatial join: tag each school with its tract_id, then count per tract
joined = gpd.sjoin(schools[["geometry"]], tracts[["tract_id","geometry"]],
                   how="left", predicate="within")
counts = (
    joined.groupby("tract_id", dropna=False).size()
    .rename("schools_count")
    .reset_index()
)

# Write to S3 clean zone as a dataset
wr.s3.to_parquet(
    df=counts,
    path=f"{S3_CLEAN}/features/tract_schools_count/",
    dataset=True,
    index=False,
    mode="overwrite",
)
print("Wrote:", f"{S3_CLEAN}/features/tract_schools_count/")
