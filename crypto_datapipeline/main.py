from src.ingestion import ingest_5s
from apscheduler.schedulers.blocking import BlockingScheduler
from src.transform import preprocessing_5s_dataframe

def main():
#Step 1:Ingestion of Raw Data
#using this scheduler to call function every 5 secs
    #scheduler = BlockingScheduler()
    #function not call just reference
    #scheduler.add_job(ingest_5s,trigger='interval',seconds=5)
    #scheduler.start()

       preprocessing_5s_dataframe()

if __name__ == "__main__":
    main()