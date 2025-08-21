import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Brewers 2025 Dashboard", layout="wide")
st.title("Milwaukee Brewers 2025 — Decomposition Dashboard")

st.markdown("""
**Tabs:**
- Overview (wins vs expected)
- Contact Quality vs Outcome (xwOBA vs wOBA)
- Bullpen (Leverage)
- Defense & Run Prevention
- Sequencing & Expected Wins

> Add processed data files to `data/processed/` and the charts will populate.
""")

# Placeholder content
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview", "Contact Quality", "Bullpen", "Defense", "Sequencing"
])

with tab1:
    st.subheader("Wins vs Expected")
    st.info("Drop a file like `team_games.parquet` into data/processed to enable this tab.")

with tab2:
    st.subheader("Contact Quality vs Outcome")
    st.info("Drop a file like `statcast_batted_balls.parquet` to compare xwOBA vs wOBA over time.")

with tab3:
    st.subheader("Bullpen (Leverage)")
    st.info("Add `bullpen_agg.csv` with gmLI/WPA to visualize leverage performance.")

with tab4:
    st.subheader("Defense & Run Prevention")
    st.info("Add `defense_agg.csv` to view OAA/DRS-like summaries.")

with tab5:
    st.subheader("Sequencing & Expected Wins")
    st.info("Add `sequencing_agg.csv` (Pythag/BaseRuns vs Actual) to populate charts.")
