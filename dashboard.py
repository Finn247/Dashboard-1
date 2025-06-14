import streamlit as st

st.set_page_config(page_title="Trading Dashboard", layout="wide")

st.title("📊 Trading Signal Dashboard")
st.markdown("Welcome to your ASX & BTC tactical trading dashboard.")

st.markdown("""
### Features Coming Online:
- ASX & BTC signal engine (daily close)
- Volatility filtering
- Trade prioritisation (max 2/day)
- Confidence scoring
- Portfolio tracking
- Rolling CAGR performance
- 35% target tracking meter
""")
