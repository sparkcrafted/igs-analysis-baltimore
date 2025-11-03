# Inclusive Growth Score (IGS) Analysis — Baltimore & Peer Cities
Comparative data analysis of inclusive growth across Baltimore and peer majority-Black U.S. cities using Mastercard IGS and Census data (2017–2024).

This ongoing project examines patterns of economic and social inclusion across **Baltimore City** and a set of **peer majority-Black cities** using Mastercard’s **Inclusive Growth Score (IGS)** data (2017–2024) and U.S. Census demographic data (2020–2024). It serves as a working research environment supporting broader findings on inclusive growth, public investment, and neighborhood transformation.

---

## 🧭 Purpose  

The goal is to understand how inclusive growth varies across neighborhoods and cities — identifying which census tracts are improving, which are lagging, and what systemic or demographic factors may explain those differences.  

This repository will continue expanding as additional data sources are integrated (e.g., housing, business, and investment data).

---

## 📁 Repository Structure  

```text
igs-analysis-baltimore/
├── data_raw/ # Original IGS + Census CSVs
├── data_clean/ # Processed/derived datasets
├── visuals/ # Exported charts/maps
├── notebooks/
│ ├── 01_ingest_and_eda.ipynb # Data ingestion & initial EDA
│ ├── 02_trend_analysis.ipynb # Year-over-year Baltimore trends
│ ├── 03_mapping.ipynb # Tract-level mapping & quartiles
│ ├── 04_clean_county_demographics.ipynb # State/county demographic prep
│ ├── 05_city_comparison.ipynb # Multi-city IGS vs. % Black
│ └── 06_city_demographic_filters.ipynb # NEW: ACS city (place) filters & visuals
├── .venv/
├── .gitignore
├── Makefile
├── requirements.txt
└── README.md
```
## 🔄 Newest Outputs (2025-11-02)

### `notebooks/06_city_demographic_filters.ipynb`
A reproducible pipeline that pulls **ACS 5-year (2023)** for every U.S. **place** (city/town), then:
- Builds the **100K+ city universe** and computes `% Black`  
  - Total pop: `B01003_001E`  
  - Black pop (alone): `B02001_003E` *(toggle to `B03002_004E` for Black, non-Hispanic)*
- Produces filtered layers (saved to `data_clean/`):
  - `cities_over100k_all.csv`
  - `cities_over100k_50pct_black.csv`
  - `cities_over100k_55pct_black.csv`
  - `cities_over100k_60pct_black.csv`
- Adds analysis/visuals:
  - City counts by **population tiers** (100k–249k, 250k–499k, 500k–999k, 1M+)
  - **Population (log) vs. % Black** scatter (peer cities highlighted)
  - **Black Representation Index** = `%Black_city / 13.6% (U.S. avg)` + distribution histogram
  - “Top 15 largest cities” table with `% Black`

**Current counts (this run):**  
Cities ≥100k: **342** | ≥50%: **15** | ≥55%: **11** | ≥60%: **8**

**Quick reads from the visuals:**
- Most 100k+ cities fall in the **100k–249k** tier.  
- **250k–1M** cities, on average, show **higher % Black** than 1M+ mega-cities (which are more racially diverse overall).  
- The Black Index histogram shows most cities are **below the U.S. average (13.6%)**, with a **long right tail** driven by majority-Black cities (e.g., Jackson, Detroit, Birmingham, etc.).


## 📊 Current Focus
- Merge IGS tract-level data (2020–2024) for Baltimore
- Compute year-over-year change, median, and IQR trends
- Generate tract-level maps (above/below median, quartiles, YoY)
- Clean and combine state demographic data (AL, GA, MD, MI, MS, TN, FL)
- Compare IGS vs. % Black population for 7 peer cities:  
  - Baltimore (MD)  
  - Detroit (MI)  
  - Memphis (TN)  
  - Jackson (MS)  
  - Birmingham (AL)  
  - New Orleans (LA)  
  - Portions of Atlanta (GA)

## 🧠 Key Insights (to date)
- Baltimore’s median IGS rose from 40 → 42 between 2020–2024, while its IQR widened — indicating more variation in inclusive growth across tracts.
- Cross-city scatterplots show no simple correlation between Black population share and IGS; South Fulton (Fulton County) scored highest on average IGS.
- Mapping output visually identifies Baltimore’s quartile spread — which neighborhoods consistently outperform or underperform median IGS values.

## 🧰 Tech Stack
Python 3.12 • pandas • numpy • matplotlib • GeoPandas • requests • pathlib • VS Code

## 📅 Project Status
✅ Initial ingestion and multi-year merging complete

✅ Trend & mapping notebooks finalized

✅ State demographics cleaned and merged

🧩 Cross-city analysis (2020–2024) complete

📈 Deeper regression and regional benchmarking — upcoming

🗺️ Urban-rural comparison & spatial joins — planned

## 🗣️ Author
Warren Jones (sparkcrafted)
📍 Baltimore, MD
🌐 sparkproservices.com
📫 wjones@sparkproservices.com

This repository continues to evolve as additional datasets and analyses are added. All results are preliminary and intended for educational and exploratory purposes.

Last updated: November 2025
