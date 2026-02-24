from src.ingestion import ingest_coins_lastdays

def main():

    coins_list= ['bitcoin','solana']
    #raw_file = ingest() #fetch n coins
    rawdaysfile = ingest_coins_lastdays(coins_list,30)

if __name__ == "__main__":
    main()