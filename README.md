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
│
├── data_raw/                     # Original IGS and Census CSVs
├── data_clean/                   # Processed and merged datasets
├── visuals/                      # Generated maps and charts
├── notebooks/
│   ├── 01_ingest_and_eda.ipynb             # Data ingestion & initial EDA
│   ├── 02_trend_analysis.ipynb             # Year-over-year Baltimore trends
│   ├── 03_mapping.ipynb                    # Tract-level mapping and quartile visuals
│   ├── 04_clean_county_demographics.ipynb  # Census demographic prep (state/county)
│   └── 05_city_comparison.ipynb            # Multi-city IGS vs. Black share analysis
├── .venv/
├── .gitignore
└── Makefile, README.md, requirements.txt
```
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
