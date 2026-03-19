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
    
    print(f"{ticker_symbol} Current Price: ${current_price:.2f}")
    print(f"Daily Change: ${daily_change:.2f} ({percent_change:.2f}%)")
else:
    print("Data not available")

# Set the output variable for GitHub Actions
# GITHUB_OUTPUT is an environment file provided by GitHub Actions
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f"{ticker_symbol} Current Price: ${current_price:.2f}", file=fh)
    print(f"Daily Change: ${daily_change:.2f} ({percent_change:.2f}%)", file=fh)
    print(f'avgo_price={current_price}', file=fh)
    print(f'avgo_change={daily_change}', file=fh)
    print(f'avgo_pct_change={percent_change}', file=fh)
