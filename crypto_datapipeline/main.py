import requests
import json
from datetime import datetime

#API

url = "https://api.coingecko.com/api/v3"

params = {
    "vs_currency": "ca",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}


#fetch data 
response = requests(url,params)
data = response.json()

#take today time in YYYY/MM/DD
today = datetime.now().strftime("%Y-%m-%d")
#create a json file with data from api and save it in data/raw
with open(f"data/raw/markets_{today}.json", "w") as f:
    json.dump(data, f, indent=2)