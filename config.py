# config.py — project-wide paths/constants

from pathlib import Path

# Detect project root whether you run from notebooks/ or the root
CWD = Path.cwd()
ROOT = CWD.parent if CWD.name == "notebooks" else CWD

RAW_SHAPES  = ROOT / "data_raw" / "shapes"
PROJ_SHAPES = ROOT / "shapes"

# Raw inputs (your filenames from earlier cells)
TRACTS_RAW  = RAW_SHAPES / "2020_Census_Tracts_(Census_TIGER).geojson"
CSAS_RAW    = RAW_SHAPES / "Community_Statistical_Areas_(CSAs)__Reference_Boundaries.geojson"

# Standardized outputs (written by your subset cell)
TRACTS_FP   = PROJ_SHAPES / "baltimore_tracts_2020.geojson"
CSAS_FP     = PROJ_SHAPES / "baltimore_csa.geojson"
