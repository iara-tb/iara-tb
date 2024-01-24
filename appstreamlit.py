import yfinance as yf
import streamlit as st
import padas as pd

st.write("""
#Simple Stock Price App

Show are the stock **clhosing price** and ***volume*** of Google!

""")
         #the ticker symbol
tickerSymbol = 'GOOGL'
#get data on ticker
tickerData= yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf= tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
#Openn high Low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)