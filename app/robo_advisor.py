import json
import requests

line = "------------------------"

# function to convert float or integer to usd-formatted string
def to_usd(my_price):
    return f"${my_price:,.2f}"

# INFO INPUTS

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
latest_close = parsed_response["Time Series (5min)"]["2021-03-05 19:55:00"]["4. close"]
# to_usd(float(latest_close))


# INFO OUTPUTS

print(line)
print("SELECTED SYMBOL: ")
print(line)
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {current_datetime}")
print(line)
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $")
print("RECENT LOW: $")
print(line)
print("RECOMMENDATION: BUY!")
print("BECAUSE: TODO")
print(line)
print("HAPPY INVESTING!")
print(line)