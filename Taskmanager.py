"""Contains Representation of task, task result, and the managers."""
import time
from multiprocessing import Pool, Queue
from typing import Callable, List, Optional
from dataclasses import dataclass
from DB import Database
from Analysis import Analysis, AnalysisManager


JSON_PATH = "analysis.json"


@dataclass
class TaskResult:
    """
    Wrapper for result returned by crawling function, e.g.
    list of next urls, html file, time taken to process, etc.
    """

    url: str
    ip_addr: str
    geolocation: str
    next_urls: List[str]
    rtt: float
    analysis: Analysis


class TaskManager:
    """
    Spawn a task pool to execute function specified in the constructor.

    # Constructor argument and decorator is incomplete,
    # function is expected to take a url string and Result Queue.
    """

    def __init__(
        self,
        db: Database,
        analysis_manager: AnalysisManager,
        function: Callable[[str], Optional[TaskResult]],
        timeout: float = 60,
        num_procs: int = 10,
        num_urls: int = 10000
    ):
        self.function = function
        self.timeout = timeout
        self.num_procs = num_procs
        self.queue: Queue[TaskResult] = Queue()
        self.db = db
        self.start_time = time.time()
        self.curr_task_id = 0
        self.running = 0
        self.finished = 0
        self.visited_urls = set()
        self.analysis_manager = analysis_manager
        self.pending_tasks_map = dict()
        self.num_urls = num_urls

    def timed_out(self) -> bool:
        """Check if timeout has been elapsed"""
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        return elapsed_time > self.timeout

    def _callback(self, result):
        print(f"Callback: {result}", flush=True)
        self.queue.put(result)

    def _error_callback(self, e):
        print("error in callback:", e)
        raise e

    def _add_tasks(self, pool: Pool, tasks: List[str]) -> None:
        for task in tasks:
            if task in self.visited_urls:
                continue
            self.running += 1
            self.visited_urls.add(task)
            # Placeholder value, to differentiate between
            # visited and unvisited urls
            self.db.set(
                self.curr_task_id,
                f"{task};;PENDING;;PENDING;;PENDING",
            )
            self.pending_tasks_map[task] = self.curr_task_id
            self.curr_task_id += 1

            pool.apply_async(
                self.function,
                args=(task,),
                callback=self._callback,
                error_callback=self._error_callback,
            )

    def _load_url_db(self):
        to_visit = []
        for key in self.db.list_keys():
            value = self.db.get(key)
            url, ip_addr, _, _ = value.split(";;")
            if ip_addr != "PENDING":
                self.visited_urls.add(url)
            else:
                print("not processed yet:", url)
                to_visit.append(url)
        return to_visit

    def start(self):
        """
        Start a task pool, the master process will collect
        the result from queue and add more tasks to the pool
        """
        seed = self._load_url_db()
        print(self.visited_urls, seed)
        self.curr_task_id = len(self.visited_urls)

        with Pool(self.num_procs) as task_pool:
            # map doesn't work somehow
            self._add_tasks(task_pool, seed)
            print(self.finished, self.running)
            while True:
                # Check if it has timed out
                if self.timed_out():
                    break

                result = self.queue.get(timeout=self.timeout)
                if not result:
                    continue 
                task_id = self.pending_tasks_map[result.url]
                print(
                    f"Task {task_id} finished, url: {result.url}, time taken: {result.rtt}"
                )
                self.db.set(
                    task_id,
                    f"{result.url};;{result.ip_addr};;{result.geolocation};;{result.rtt}",
                )
                self.analysis_manager.add(result.analysis)

                # Process next urls
                if self.curr_task_id < self.num_urls:
                    self._add_tasks(task_pool, result.next_urls)
                self.finished += 1

        print("Terminating...")
        self.tear_down()

    def tear_down(self):
        # analysis manager stores to json file
        self.analysis_manager.store(JSON_PATH)
