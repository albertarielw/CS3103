from Taskmanager import TaskManager, JSON_PATH
from Webcrawler import Webcrawler
from DB import FileDB
from pathlib import Path 
from Analysis import AnalysisManager
import signal
import sys

DB_NAME = "database.txt"

TIMEOUT = 600 # timeout in second until the crawler terminate 
NUM_PROCS = 10 # number of process spawned (excluding the main process)
NUM_URLS = 10000 # maximum number of urls to visit 


def main():
    crawler = Webcrawler()
    analysis_manager = AnalysisManager()
    if Path(JSON_PATH).is_file():
        analysis_manager.load(JSON_PATH) 
    
    taskmanager = TaskManager(
        db=FileDB(DB_NAME),
        analysis_manager=analysis_manager,
        function=crawler.crawl,
        timeout=TIMEOUT,
        num_procs=NUM_PROCS,
        num_urls=NUM_URLS
    )

    def signal_handler(sig, frame):
        print("cleanup...")
        taskmanager.tear_down()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        taskmanager.start()
    except KeyboardInterrupt:
        taskmanager.tear_down()
    except Exception as e:
        print(f"error: {e}") 

if __name__ == "__main__":
    main()
