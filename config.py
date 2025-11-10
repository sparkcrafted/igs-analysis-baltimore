# config.py — project-wide paths/constants

from pathlib import Path

# --- Detect project root whether run from notebooks/ or repo root ---
CWD = Path.cwd()
ROOT = CWD.parent if CWD.name == "notebooks" else CWD

# --- Local paths -----------------------------------------------------
RAW_SHAPES  = ROOT / "data_raw" / "shapes"
PROJ_SHAPES = ROOT / "shapes"

# Raw local inputs
TRACTS_RAW  = RAW_SHAPES / "2020_Census_Tracts_(Census_TIGER).geojson"
CSAS_RAW    = RAW_SHAPES / "Community_Statistical_Areas_(CSAs)__Reference_Boundaries.geojson"

# Standardized outputs (written by your subset cell)
TRACTS_FP   = PROJ_SHAPES / "baltimore_tracts_2020.geojson"
CSAS_FP     = PROJ_SHAPES / "baltimore_csa.geojson"

# --- S3 paths (use a single base, then derive zones) ---
S3_BUCKET   = "dataeng-landing-wj"
S3_BASE     = f"s3://{S3_BUCKET}"

S3_RAW      = f"{S3_BASE}/raw"
S3_CLEAN    = f"{S3_BASE}/clean"
S3_CURATED  = f"{S3_BASE}/curated"

# Large tabular datasets (RAW zone)
S3_ASEC_PPPUB24 = f"{S3_RAW}/pppub24.csv"
S3_ASEC_REPWGT  = f"{S3_RAW}/asec_csv_repwgt_2024.csv"
S3_CBP_CO       = f"{S3_RAW}/cbp23co.txt"
S3_CBP_MSA      = f"{S3_RAW}/cbp23msa.txt"
S3_ZBP_DETAIL   = f"{S3_RAW}/zbp23detail.txt"

# Optional RAW mirrors for shapes
S3_SHAPES_TRACTS = f"{S3_RAW}/shapes/2020_Census_Tracts_(Census_TIGER).geojson"
S3_SHAPES_CSAS   = f"{S3_RAW}/shapes/Community_Statistical_Areas_(CSAs)__Reference_Boundaries.geojson"
