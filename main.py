from Taskmanager import TaskManager, JSON_PATH
from Webcrawler import Webcrawler
from DB import FileDB
from pathlib import Path 
from Analysis import AnalysisManager
import signal
import sys

DB_NAME = "database.txt"


def main():
    crawler = Webcrawler()
    analysis_manager = AnalysisManager()
    if Path(JSON_PATH).is_file():
        analysis_manager.load(JSON_PATH) 
    
    taskmanager = TaskManager(
        db=FileDB(DB_NAME),
        analysis_manager=analysis_manager,
        function=crawler.crawl,
        timeout=600,
        num_procs=10,
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
