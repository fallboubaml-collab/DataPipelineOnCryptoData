import requests
import json
from datetime import datetime
import os
import time

#Make it a function to call it later on main.py it is a demo
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
    
def ingest_coins_lastdays(coins: list, last_days: int = 30):

    # Project root
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RAW_FOLDER =  os.path.join(PROJECT_ROOT, "data", "raw")

    #loot in all coin 
    for coin in coins:

        url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
        params = {
            "vs_currency": "cad",
            "days": last_days,
            "interval": "daily",
            "id": coin,
            "name":coin,
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Failed for {coin}: {response.status_code}")
            continue

        data = response.json()

        file_path = os.path.join(RAW_FOLDER, f"{coin}_last{last_days}days.json")

        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

        print(f"Saved {coin} historical data to {file_path}")

 
def ingest_5s():
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
#take  time in YYYY/MM/DD/H/M/S
    call5s= datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

 # Find project root (parent folder of src/)
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RAW_FOLDER = os.path.join(PROJECT_ROOT, "data", "raw",'MFC')
    filename = os.path.join(RAW_FOLDER, f"markets_{call5s}.json")

#create a json file with data from api and save it in data/raw
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

        print(filename)
        time.sleep(2)




 
    



