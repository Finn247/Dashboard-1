import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="ASX & BTC Trading Dashboard", layout="wide")
st.title("📈 Tactical Trading Dashboard")
st.markdown("Live signal engine for ASX (Top 20 excluded) and Bitcoin. Updated EOD with prioritised trades.")

# Simulated trade signals (to be replaced with real logic)
asx_signals = pd.DataFrame({
    'Ticker': ['SGR.AX', 'NEC.AX'],
    'Signal': ['Buy', 'Hold'],
    'Confidence': [0.87, 0.52],
    'Entry Price': [1.23, 2.45],
    'Position Size (%)': [35, 0],
    'Trade Date': [datetime.date.today()] * 2
})

btc_signals = pd.DataFrame({
    'Asset': ['BTC-USD'],
    'Signal': ['Sell'],
    'Confidence': [0.68],
    'Entry Price': [68750],
    'Position Size (%)': [20],
    'Trade Date': [datetime.date.today()]
})

st.header("📊 ASX Signal Summary")
st.dataframe(asx_signals)

st.header("₿ BTC Signal Summary")
st.dataframe(btc_signals)

st.markdown("Last update: **{} AEST**".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
