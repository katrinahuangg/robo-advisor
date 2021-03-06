import json
import requests

line = "------------------------"

# INFO INPUTS

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
response = requests.get(request_url)


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


#print(type(response)) #> <class 'requests.models.Response'>
#print(response.status_code) #> 200
#print(response.text)

# INFO OUTPUTS

print(line)
print("SELECTED SYMBOL: ")
print(line)
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: time")
print(line)
print(f"LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: $")
print("RECENT HIGH: $")
print("RECENT LOW: $")
print(line)
print("RECOMMENDATION: BUY!")
print("BECAUSE: TODO")
print(line)
print("HAPPY INVESTING!")
print(line)