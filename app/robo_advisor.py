import csv
import json
import os

from dotenv import load_dotenv
import requests

load_dotenv()

# initialize variables
line = "------------------------"
selected_tickers = []
high_prices = []
low_prices = []
key = "Meta Data"

# function to convert float or integer to usd-formatted string
def to_usd(my_price):
    return f"${my_price:,.2f}"

# INFO INPUTS
while True:
    ticker = input("Please input a stock or cryptocurrency symbol one at a time or type DONE: ")
    # break loop if user input is 'DONE'
    if ticker.upper() == "DONE":
        break
    # validate other entries
    else:
        if ticker.isalpha() == False or len(str(ticker)) > 5:
                print("Sorry, the symbol you have entered is not valid. Make sure that the ticker only contains letters and is a valid length. Please try again.")
        else:
            # add selected ticker to list if valid
            selected_tickers.append(ticker)


# get current request time and date
from datetime import datetime
now = datetime.now()
current_datetime = now.strftime("%m-%d-%Y %I:%M %p")

for ticker in selected_tickers:
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    ticker = ticker.upper()
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={api_key}"
    response = requests.get(request_url)

    parsed_response = json.loads(response.text)

    if key not in parsed_response.keys():
        print(f"Sorry, couldn't find {ticker} data.")
        continue
    else:
        # get last refreshed date and time
        last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

        # get latest close
        ts = parsed_response["Time Series (5min)"]
        dates = list(ts.keys()) #TODO sort to ensure latest day is first
        latest_day = dates[0]
        latest_close = ts[latest_day]["4. close"]

        # get recent close (max of all high prices)

        for date in dates:
            high_price = ts[date]["2. high"]
            high_prices.append(float(high_price))
            low_price = ts[date]["3. low"]
            low_prices.append(float(low_price))
        
        recent_high = max(high_prices)
        recent_low = min(low_prices)

        # csv file writing
        csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", f"prices.{ticker}.csv")
        csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

        with open(csv_file_path, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()
            for date in dates:
                prices = ts[date]
                writer.writerow({
                    "timestamp": date,
                    "open": prices["1. open"],
                    "high": prices["2. high"], 
                    "low": prices["3. low"], 
                    "close": prices["4. close"], 
                    "volume": prices["5. volume"]
                })

        if float(latest_close) < (float(recent_low) * 1.2): # if latest close is less than 1.2x recent low
            recommendation = "BUY"
            recommendation_explanation = "THE STOCK'S LATEST CLOSE IS LESS THAN 20% ABOVE THE RECENT LOW."
        else:
            recommendation = "DO NOT BUY"
            recommendation_explanation = "THE STOCK PRICE IS TOO EXPENSIVE."

        # INFO OUTPUTS
        print(line)
        print(f"SELECTED SYMBOL: {ticker}")
        print(line)
        print("REQUESTING STOCK MARKET DATA...")
        print(f"REQUEST AT: {current_datetime}")
        print(line)
        print(f"LATEST DAY: {last_refreshed}")
        print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
        print(f"RECENT HIGH: {to_usd(float(recent_high))}")
        print(f"RECENT LOW: {to_usd(float(recent_low))}")
        print(line)
        print(f"RECOMMENDATION: {recommendation}!")
        print(f"BECAUSE: {recommendation_explanation}")
        print(line)
        print(f"WRITING DATA TO CSV: {csv_file_path}...")
        print(line)
        print("HAPPY INVESTING!")
        print(line)


