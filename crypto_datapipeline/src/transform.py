import pandas as pd
import json
import glob
import os


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



def loading_5sec_pd():
    folder_path = "../data/raw/MFC"

    #hold json file in folder
    json_files = glob.glob(os.path.join(folder_path, "*.json"))
    print("Files found:", len(json_files))

    list_of_dfs = []

        #iterate in all file to convert as a df in list_of_df
    for file_path in json_files:
        try:
            df = pd.read_json(file_path, lines=True)
            list_of_dfs.append(df)
        except Exception as e:
             print(f"Failed on {file_path}: {e}")

    #list of df concatonate df to make a full on dataframe of all df
    if list_of_dfs:
        master_df = pd.concat(list_of_dfs, ignore_index=True)
        print("Final shape:", master_df.shape)
        display(master_df.head())
    else:
     print("No valid JSON data loaded.")
     return master_df
    


def preprocessing_5s_dataframe():

    #load df
    df = loading_5sec_pd()
    #drop NAN value
    df.dropna()

    # Folder to save processed DataFrame
    output_folder = "../data/processed"
    os.makedirs(output_folder, exist_ok=True)

    # File path
    output_file = os.path.join(output_folder, "mdf_data.csv")

    # Save DataFrame
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")






 
    


