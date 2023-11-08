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
        function: Callable[[str], Optional[TaskResult]],
        seed: list[str],
        timeout: float = 10,
        num_procs: int = 10,
        analysis_manager: AnalysisManager = AnalysisManager()
    ):
        self.function = function
        self.seed = seed
        self.timeout = timeout
        self.num_procs = num_procs
        self.queue: Queue[TaskResult] = Queue()
        self.db = db
        self.start_time = time.time()
        self.task_id = 0
        self.running = len(seed)
        self.finished = 0
        self.visited_urls = set()
        self.analysis_manager = analysis_manager

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
            pool.apply_async(
                self.function,
                args=(task,),
                callback=self._callback,
                error_callback=self._error_callback,
            )

    def start(self):
        """
        Start a task pool, the master process will collect
        the result from queue and add more tasks to the pool
        """
        with Pool(self.num_procs) as task_pool:
            # map doesn't work somehow
            self._add_tasks(task_pool, self.seed)

            while self.finished < self.running:
                # Check if it has timed out
                if self.timed_out():
                    break

                result = self.queue.get(timeout=self.timeout)
                print(
                    f"Task {self.task_id} finished, url: {result.url}, time taken: {result.rtt}"
                )
                self.visited_urls.add(result.ip_addr)
                self.db.set(
                    self.task_id,
                    f"{result.url};;{result.ip_addr};;{result.geolocation};;{result.rtt}",
                )
                self.analysis_manager.add(result.analysis)
                self.task_id += 1

                # Process next urls
                self._add_tasks(task_pool, result.next_urls)
                self.finished += 1
                self.running += len(result.next_urls)
        
        print("Terminating...")
        self.tear_down()
    
    def tear_down(self): 
        #analysis manager stores to json file
        self.analysis_manager.store(JSON_PATH)
        
