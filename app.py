import yfinance as yf
import streamlit as st
import datetime

# App title
st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of a selected stock!
""")

# Sidebar for user input
st.sidebar.header("User Input")
tickerSymbol = st.sidebar.text_input("Enter Stock Ticker Symbol", "GOOGL")
start_date = st.sidebar.date_input("Start Date", datetime.date(2010, 5, 31))
end_date = st.sidebar.date_input("End Date", datetime.date(2020, 5, 31))

# Fetch stock data
try:
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

    # Display closing price
    st.write(f"""
    ## {tickerSymbol} Closing Price
    """)
    st.line_chart(tickerDf.Close)

    # Display volume
    st.write(f"""
    ## {tickerSymbol} Volume
    """)
    st.line_chart(tickerDf.Volume)
except Exception as e:
    st.error(f"Error fetching data for {tickerSymbol}: {e}")