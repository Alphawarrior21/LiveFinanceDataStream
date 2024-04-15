Bollinger Bands are a technical analysis tool developed by John Bollinger in the 1980s. It is used by traders to gauge potential price movements. Figure below shows a sample 20-day rolling average for a stock and it’s corresponding bollinger bands.

![image](https://github.com/Alphawarrior21/LiveFinanceDataStream/assets/30016067/a1aa3000-22b0-4265-8d8f-b1b5464d4676)

**Set Up**

yfinance is a Python library that provides a simple interface for accessing historical market data, real-time data, and other financial information from Yahoo Finance. It allows users to easily retrieve data such as historical stock prices, dividends, corporate actions, and more. Run the following command to install yfinance.

pip install yfinance

**Understanding Bollinger Bands**

Bollinger Bands consist of three lines plotted on a price chart: a middle line representing a simple moving average (typically calculated over 20 periods), and an upper and lower band that are typically two standard deviations away from the moving average. The bands are dynamically adjusted according to volatility, expanding and contracting as market volatility increases or decreases.

Here’s a breakdown of the components of Bollinger Bands:

Middle Line (Simple Moving Average):
The middle line of the Bollinger Bands is a simple moving average (SMA) of the closing prices over a specified period (usually 20 periods).
It serves as a baseline representing the average price of the security over the selected period.
2. Upper Band:

The upper band is calculated by adding two standard deviations to the middle line.
It represents the upper boundary of expected price movements.
It tends to act as a resistance level during uptrends.
3. Lower Band:

The lower band is calculated by subtracting two standard deviations from the middle line.
It represents the lower boundary of expected price movements.
It tends to act as a support level during downtrends.

**Interpretation and Use:**

Volatility Measurement: Bollinger Bands expand and contract based on market volatility. Wide bands indicate high volatility, while narrow bands suggest low volatility.
Overbought and Oversold Conditions: When the price touches or exceeds the upper band, it may indicate that the security is overbought, and a reversal or pullback could occur. Conversely, when the price touches or falls below the lower band, it may indicate that the security is oversold, and a potential reversal to the upside could occur.
Trend Confirmation: Bollinger Bands can be used to confirm trends identified by other indicators or analysis methods. In an uptrend, the price tends to hug the upper band, while in a downtrend, it tends to stay near the lower band.
Trading Signals: Traders often use Bollinger Bands to identify entry and exit points for trades. For example, buying when the price touches the lower band and selling when it touches the upper band (or vice versa).

Overall, Bollinger Bands are a versatile tool used by traders and analysts to assess market volatility, identify potential reversals, confirm trends, and generate trading signals. They provide valuable insights into price action and can be incorporated into various trading strategies across different financial markets.

**Plotting Bollinger Bands using Python**

We will need to fetch stock data using the Yahoo Finance API (yfinance), convert it into a structured format using the Pandas library, and then visualize it along with Bollinger Bands using matplotlib.

Fetching Stock Data:

def fetch_stock_data(stock_symbol):
    try:
        # Fetching stock data
        stock = yf.Ticker(stock_symbol)
        stock_data = stock.history(period="12mo")

        # Convert 'Close' column to numeric
        stock_data['Close'] = pd.to_numeric(stock_data['Close'])
    
        return stock_data
    except Exception as e:
        print("Error fetching stock data:", str(e))
        return None

        
The function fetch_stock_data(stock_symbol) takes a stock symbol as input parameter.
It utilizes the yfinance library to fetch historical stock data for the specified symbol over the past 12 months (period="12mo").
The ‘Close’ column of the stock data is converted to numeric format.

Now let’s try running this method for TATASTEEL and examine the response.

stock_data = fetch_stock_data(stock_symbol='TATASTEEL.NS')
print(stock_data.head())

![image](https://github.com/Alphawarrior21/LiveFinanceDataStream/assets/30016067/95975d8f-4b59-408d-86ac-f696905b356c)

Plotting Bollinger Bands:

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

    
The function plot_bollinger_bands(stock_data) takes the fetched stock data as input.
It creates a matplotlib figure and plots the closing price of the stock.
It calculates the 20-day rolling average of the stock’s closing price and plots it.
It calculates the upper and lower Bollinger Bands based on the 20-day rolling average and standard deviation.
These bands are then plotted along with the closing price.

![image](https://github.com/Alphawarrior21/LiveFinanceDataStream/assets/30016067/e49814d6-04a2-4aa8-8865-9a8eed9d6563)






