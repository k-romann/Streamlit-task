import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib as plt


st.write("""# Company quote data
Shown how Apple stock prices have changed!
""")

tickerSymbol = "AAPL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id', start='2008-1-01', end='2018-12-31')

st.write('''
### Price per share after the opening of trading
''')
st.line_chart(tickerDf.Open)

st.write('''
### Price per share after the close of trading
''')
st.line_chart(tickerDf.Close)
