import yfinance as yf
import os

# Get ticker data
avgo = yf.Ticker("AVGO")

# Get fast info for price and daily change
info = avgo.info
current_price = info.get('currentPrice')
prev_close = info.get('previousClose')

if current_price and prev_close:
    daily_change = current_price - prev_close
    percent_change = (daily_change / prev_close) * 100
    
    print(f"Current Price: ${current_price:.2f}")
    print(f"Daily Change: ${daily_change:.2f} ({percent_change:.2f}%)")
    #  the $  here is a $ character, not a variable indicator like in the yaml file
    str1 = f"${current_price:.2f}"
    str2 = f"${daily_change:.2f}"
    str3 = f"{percent_change:.2f}"
else:
    print("Data not available")

# Set the output variable for GitHub Actions
# GITHUB_OUTPUT is an environment file provided by GitHub Actions
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'avgo_price={str1}', file=fh)
    print(f'avgo_change={str2}', file=fh)
    print(f'avgo_pct_change={str3}', file=fh)
