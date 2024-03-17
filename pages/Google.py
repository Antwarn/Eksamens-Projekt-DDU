import yfinance as yf
import streamlit as st

def display_google():
    st.header("Google")
    st.write("### Google's aktier fra starten af 2023")
    google = 'GOOG'
    #get data on this ticker
    tickerData = yf.Ticker(google)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2023-1-1', end='2024-3-15')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.line_chart(tickerDf.Close)
    #st.line_chart(tickerDf.Volume)