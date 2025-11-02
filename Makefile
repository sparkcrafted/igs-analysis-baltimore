# ======================================
# Baltimore IGS Analysis Automation
# ======================================

PY := .venv/bin/python

run:
	@echo "Running data cleaning notebook..."
	$(PY) -m jupyter nbconvert --to notebook --execute notebooks/01_data_cleaning.ipynb --output notebooks/01_data_cleaning_executed.ipynb

	@echo "Running trend analysis notebook..."
	$(PY) -m jupyter nbconvert --to notebook --execute notebooks/02_trend_analysis.ipynb --output notebooks/02_trend_analysis_executed.ipynb

	@echo "All notebooks executed. Outputs saved in data_clean/ and visuals/."
