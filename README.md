# Brewers 2025 Success Analysis

**Goal:** quantify why the Milwaukee Brewers are winning in 2025 using Statcast and sabermetric models.

## Focus Areas
- **Expected vs Actual Wins:** Pythagorean & BaseRuns vs real outcomes.
- **Contact Quality vs Outcome:** Statcast xwOBA vs wOBA (team & hitters).
- **Bullpen in Leverage:** WPA, gmLI, rest patterns.
- **Defense & Run Prevention:** OAA/DRS proxies, park & schedule context.
- **Sequencing:** RISP vs bases-empty, late/close splits.

## Repo Layout
```
brewers-2025-analysis/
├─ data/                 # raw/processed parquet & csv (not tracked)
├─ notebooks/            # exploratory notebooks
├─ src/                  # python package: ingest/clean/features/models/viz
├─ reports/              # writeup (markdown)
└─ app/                  # Streamlit dashboard
```

## Quickstart
1) Create and activate a Python 3.10+ env (uv/venv/conda).

2) Install: `pip install -e .`

3) Run data pulls (coming soon): `python -m src.ingest`

4) Launch the app: `streamlit run app/streamlit_app.py`

## Tech Stack
Python · pandas · duckdb · pyarrow · scikit-learn · statsmodels · plotly · streamlit · pybaseball

## License
MIT
