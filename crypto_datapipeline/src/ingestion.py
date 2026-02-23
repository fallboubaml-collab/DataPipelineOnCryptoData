import requests
import json
from datetime import datetime
import os

#Make it a function to call it later on main.py
def ingest(top=10):
#API gecko
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
    "vs_currency": "cad",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
    }
#fetch data 
    response = requests.get(url,params)
    data = response.json()
#take today time in YYYY/MM/DD
    today = datetime.now().strftime("%Y-%m-%d")

 # Find project root (parent folder of src/)
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RAW_FOLDER = os.path.join(PROJECT_ROOT, "data", "raw")
    filename = os.path.join(RAW_FOLDER, f"markets_{today}.json")

#create a json file with data from api and save it in data/raw
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

        print(filename)

        return filename