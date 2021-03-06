import json
import requests

# INFO INPUTS

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
response = requests.get(request_url)


parsed_response = json.loads(response.text)


print(type(response))
print(response.status_code)
print(response.text)

quit()

print("Hello")
print("Is this working")