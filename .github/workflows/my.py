import yfinance as yf

# Get ticker data
aapl = yf.Ticker("AVGO")

# Get current price
price = aapl.info['currentPrice']
print(f"AVGO quote: {price}")
