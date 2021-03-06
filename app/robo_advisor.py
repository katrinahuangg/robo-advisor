import csv
import json
import os

import requests


line = "------------------------"

# function to convert float or integer to usd-formatted string
def to_usd(my_price):
    return f"${my_price:,.2f}"

# INFO INPUTS
while True:
    ticker = input("Please input a stock or cryptocurrency symbol: ")
    # break loop if user input is 'DONE'
    if selected_id.upper() == "DONE":
        break
    # validate other entries
    else:
        if selected_id not in valid_ids:
            print("Sorry, the product identifier you have entered is not valid. Please try again.")
        else:
            # add selected id to list if valid
            selected_ids.append(selected_id)



request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
response = requests.get(request_url)


parsed_response = json.loads(response.text)

# get last refreshed date and time
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

# get current request time and date
from datetime import datetime
now = datetime.now()
current_datetime = now.strftime("%m-%d-%Y %I:%M %p")

# get latest close
ts = parsed_response["Time Series (5min)"]
dates = list(ts.keys()) #TODO sort to ensure latest day is first
latest_day = dates[0]
latest_close = ts[latest_day]["4. close"]

# get recent close (max of all high prices)
high_prices = []
low_prices = []

for date in dates:
    high_price = ts[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = ts[date]["3. low"]
    low_prices.append(float(low_price))
recent_high = max(high_prices)
recent_low = min(low_prices)



# csv file writing
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
csv_headers = ["city", "name"]

with open(csv_file_path, "W") as csv_file:
    writer = csv.DictWriter(csv_file, filednames=csv_headers)
    writer.writeheader()

    writer.writerow({"city": "New York", "name": "Yankees"})

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
print("RECOMMENDATION: BUY!")
print("BECAUSE: TODO")
print(line)
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print(line)
print("HAPPY INVESTING!")
print(line)

