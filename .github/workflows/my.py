import yfinance as yf
import os

# Get ticker data
aapl = yf.Ticker("AVGO")

# Get current price
price = aapl.info['currentPrice']
print(f"AVGO quote: {price}")

# Set the output variable for GitHub Actions
# GITHUB_OUTPUT is an environment file provided by GitHub Actions
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'my_output_variable={price}', file=fh)
