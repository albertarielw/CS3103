from Taskmanager import TaskManager
from Webcrawler import Webcrawler
from DB import FileDB

DB_NAME = "database.txt"


def main():
    crawler = Webcrawler()
    # TODO optional: initialize AnalysisManager from a json file
    taskmanager = TaskManager(
        db=FileDB(DB_NAME),
        function=crawler.crawl,
        timeout=60,
        num_procs=10,
    )
    taskmanager.start()


if __name__ == "__main__":
    main()
