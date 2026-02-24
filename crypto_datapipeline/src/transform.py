import pandas as pd
import json

#Function to transform to dataframe
def loading_in_pd(day):

    time_frame = day
    #Load raw JSON
    with open("data/raw/{time_frame}.json") as f:
        data = json.load(f)
    #transform to Dataframe
    df = pd.DataFrame(data)

    # Keep relevant columns
    df = df[['id','symbol','name','current_price','market_cap','total_volume','price_change_percentage_24h']]

    return df



def preprocessing_dataframe():

    df = loading_in_pd('markets_2026-02-23.json')
    #the data is mostly well organize so missing value mostly
    df.fillna(0,inplace=True)

    #this more but that is more like learning the process not doing it.I use data_analysis to run analysis on data to see what to automate
    #The CoinGecko is structured meanly so no much cleaning

    #save in a csv
    df.to_csv("data/processed/{time_frame}", index=False)


def loading_coins_pd(coins="bitcoin",lastdays=30):

    #Load raw JSON
    with open(f"data/raw/{coins}last{lastdays}days.json") as f:
        data = json.load(f)
    #transform to Dataframe
    df = pd.DataFrame(data)

    # Keep relevant columns
    df = df[['id','symbol','name','current_price','market_cap','total_volume','price_change_percentage_24h']]

    return {
        "data": df,
        "coin": coins,
        "days": lastdays
    }




