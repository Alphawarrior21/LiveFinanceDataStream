from datetime import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(stock_symbol):
    try:
        # Fetching stock data
        stock = yf.Ticker(stock_symbol)
        stock_data = stock.history(period="12mo")
        #print(stock_data.head())

        # Convert 'Close' column to numeric
        stock_data['Close'] = pd.to_numeric(stock_data['Close'])
    
        return stock_data
    except Exception as e:
        print("Error fetching stock data:", str(e))
        return None
    


def plot_bollinger_bands(stock_data):
    plt.figure(figsize=(12, 6))
    
    # Plotting stock closing price
    plt.plot(stock_data['Close'], label='Close Price')

    plt.figure(figsize=(12, 6))
    # Calculating and plotting 20-day rolling average
    stock_data['MA20'] = stock_data['Close'].rolling(window=20).mean()
    plt.plot(stock_data['MA20'], label='20-Day Rolling Average')

    # Calculating and plotting Bollinger Bands
    stock_data['20D_MA'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['Upper_band'] = stock_data['20D_MA'] + 2 * stock_data['Close'].rolling(window=20).std()
    stock_data['Lower_band'] = stock_data['20D_MA'] - 2 * stock_data['Close'].rolling(window=20).std()
    plt.plot(stock_data['Upper_band'], label='Upper Bollinger Band', linestyle='--', color='red')
    plt.plot(stock_data['Lower_band'], label='Lower Bollinger Band', linestyle='--', color='green')
    
    plt.title('Stock Data with Rolling Average and Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

#Fetch data for a particular stock
stock_data = fetch_stock_data(stock_symbol='TATASTEEL.NS')
print(stock_data.head())
plot_bollinger_bands(stock_data)



    