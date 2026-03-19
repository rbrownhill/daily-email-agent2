import yfinance as yf
import os
import requests
import json

# STOCK QUOTE SECTION

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

#  AI MODEL SECTION

def call_ai_studio(prompt_text):
    # Get key from environment (stored in GitHub Secrets)
    api_key = os.getenv("GOOGLE_API_KEY")
    url = "https://generativelanguage.googleapis.com"
    # Pass the API key as a parameter; requests will handle the '?' and '=' correctly
    params = {'key': api_key}
    
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": prompt_text}]}]
    }

    response = requests.post(url, headers=headers, json=data, params=params)
    
    if response.status_code == 200:
        # Extract response text
        result = response.json()['candidates'][0]['content']['parts'][0]['text']
        return result.replace('\n', ' ').strip()
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    try:
        # Example: Calling it twice for different tasks
        stoic = call_ai_studio("provide me a quote by using an api call to endpoint https://stoic-quotes.com/api/quotes.  return just the quote..")
        bet = call_ai_studio("find a specific example of an illogical bet that is active on a betting website such as kalshi or polymarket. choose one at random so that your reply is likely to be different from yesterday. make your response brief.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

# OUTPUT SECTION
# GITHUB_OUTPUT is an environment file provided by GitHub Actions
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'avgo_price={str1}', file=fh)
    print(f'avgo_change={str2}', file=fh)
    print(f'avgo_pct_change={str3}', file=fh)
    print(f'stoic_quote={stoic}', file=fh)
    print(f'bet_text={bet}', file=fh)
