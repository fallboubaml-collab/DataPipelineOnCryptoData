from src.ingestion import ingest_5s
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
#Step 1:Ingestion of Raw Data
#using this scheduler to call function every 5 secs
    scheduler = BlockingScheduler()
    #function not call just reference
    scheduler.add_job(ingest_5s,trigger='interval',seconds=5)
    scheduler.start()
       

if __name__ == "__main__":
    main()