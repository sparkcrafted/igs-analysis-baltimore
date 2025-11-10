# Inclusive Growth Score (IGS) Analysis — Baltimore & Peer Cities
Comparative analysis of inclusive growth across **Baltimore** and peer majority-Black U.S. cities using Mastercard IGS, Census/ACS, and neighborhood-scale community indicators (2017–2025).

This project examines patterns of economic and social inclusion across **census tracts** and **Community Statistical Areas (CSAs)**. It extends from tract-level IGS metrics to CSA-level social indicators (poverty, education, access to services) to reveal how place-based conditions intersect with growth and equity.

---

## 🧭 Purpose
Understand **where** inclusive growth is happening (and where it isn’t) and **why** — by linking IGS trends with community indicators such as child poverty, education, financial access, and food access.

---

## 📁 Repository Structure
```text
igs-analysis-baltimore/
├── data_raw/               # Original IGS / ACS / community CSVs & GeoJSON (not tracked)
├── data_intermediate/      # Caches (e.g., geocoded points) (not tracked)
├── data_clean/             # Processed datasets (e.g., *.parquet)
├── visuals/                # Exported charts/maps
├── shapes/                 # GeoJSON boundaries (tracts, CSAs)
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_trend_analysis.ipynb
│   ├── 03_mapping.ipynb
│   ├── 04_clean_county_demographics.ipynb
│   ├── 05_city_comparison.ipynb
│   ├── 06_city_demographic_filters.ipynb
│   ├── 07_place_analysis.ipynb
│   ├── 08_economy_analysis.ipynb
│   └── 09_community_analysis.ipynb   # NEW: Baltimore CSA feature engineering & visuals
├── .vscode/                # VS Code settings (type-check tuning)
├── Makefile
├── requirements.txt
└── README.md
```
## 🆕 Newest Work (Nov 2025): Community Statistical Areas (CSAs)
Notebook: notebooks/09_community_analysis.ipynb
Ingests CSA-keyed tables:
* Median household income
* % children in poverty
* % adults with HS or some college
* % adults with < HS diploma
* Average household size
* Banks per 1,000 residents
* Converts point datasets to counts per CSA via spatial join:
* Grocery stores, farmers markets (schools/libraries optional)

Produces:
* data_clean/csa_features.parquet (wide table by CSA)
* Choropleths (income, poverty, grocery access) and a correlation heatmap
* Tract-level engineering previously produced data_clean/tract_features_wide.parquet.
* Why it matters: connects economic outcomes (IGS) with community conditions at a neighborhood scale.

## 📊 Current Focus
* Finalize CSA dashboard (maps + correlations) for Baltimore
* Link tract IGS to CSA context for multilevel comparisons
* Scale the CSA/tract workflow across peer cities (Detroit, Jackson, Memphis, etc.)
* Begin regression & clustering to detect structural patterns

## 🧠 Early Insights
* Baltimore’s median IGS rose 40 → 42 (2020–2024) while dispersion widened — gains are uneven.
* CSA correlations suggest child poverty and education track with access to services (banks/markets).
* Spatial clusters of exclusion are persistent in East/Southwest Baltimore; peer cities show similarly uneven patterns.

## 🧰 Tech Stack
Python 3.12 • pandas • numpy • matplotlib • seaborn • GeoPandas • shapely • requests • pathlib • VS Code

## 📝 Project Status
✅ IGS ingestion, cleaning, and tract mapping
✅ Cross-city IGS trends + ACS city filters
✅ CSA feature engineering for Baltimore
🧩 CSA–tract linkage & dashboards in progress
📈 Modeling (regression/cluster) upcoming

## 👤 Author
Warren Jones (sparkcrafted) — Baltimore, MD, USA
🌐 https://sparkproservices.com • 📫 wjones@sparkproservices.com
All results are preliminary and intended for research/educational use. 
Last updated: Nov 2025.
