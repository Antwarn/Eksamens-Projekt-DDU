import yfinance as yf
import streamlit as st
import matplotlib
import csv
import numpy as np



def display_apple():
    st.header("Apple")
    
    with open('stockinfo.csv', 'r') as csvfile:


        data = []
    
        csv_reader = csv.reader(csvfile)

        line_number = 0

        for row in csv_reader:
            line_number += 1
            if line_number % 6 == 0:
                

        
                price = row[2]
                volume = row[3]
                mc = row[4]
                x = [price, volume, mc]
                data.append(x)








    '''st.write("### Apple's aktier fra starten af 2023")
    apple = 'aapl'
    #get data on this ticker
    tickerData = yf.Ticker(apple)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2023-1-1', end='2024-3-15')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.line_chart(tickerDf.Close)
    #st.line_chart(tickerDf.Volume)'''
