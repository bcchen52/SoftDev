import requests
import json
import time


response_API = requests.get("https://opensky-network.org/api/states/all?time=1458564121&icao24=3c6444")
data = response_API.text
json.loads(data)
print(data)

time = pase
t1 = time.gmtime(data[0])
print(t1)