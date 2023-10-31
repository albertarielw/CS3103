from multiprocessing import Pool, Queue, Value
from typing import Callable, List
from functools import partial
from dataclasses import dataclass
from DB import Database, FileDB
import time


def result_callback(result, queue):
    print(result, queue)
    print(f"Callback got: {result}", flush=True)


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
    html_file: str
    rtt: float


class TaskManager:
    """
    Spawn a task pool to execute function specified in the constructor.

    # Constructor argument and decorator is incomplete,
    # function is expected to take a url string and Result Queue.
    """

    def __init__(
        self,
        db: Database,
        function: Callable[[str], TaskResult],
        seed: list[str],
        timeout: float = 10,
        num_procs: int = 10,
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

    def timed_out(self) -> bool:
        """Check if timeout has been elapsed"""
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        return elapsed_time > self.timeout

    def _callback(self, result):
        print(f"Callback: {result}", flush=True)
        self.queue.put(result)

    def start(self):
        """
        Start a task pool, the master process will collect
        the result from queue and add more tasks to the pool
        """
        with Pool(self.num_procs) as task_pool:
            # map doesn't work somehow
            for url in self.seed:
                # callback handles sending to queue
                task_pool.apply_async(
                    self.function, args=(url,), callback=self._callback
                )

            while self.finished < self.running:
                # Check if it has timed out
                if self.timed_out():
                    break

                result = self.queue.get(timeout=self.timeout)
                print(
                    f"Task {self.task_id} finished, url: {result.url}, time taken: {result.rtt}"
                )
                self.db.set(
                    self.task_id,
                    f"{result.url},{result.ip_addr},{result.geolocation},{result.rtt}",
                )
                self.task_id += 1

                # Process next urls
                for url in result.next_urls:
                    task_pool.apply_async(
                        self.function, args=(url,), callback=self._callback
                    )

                self.finished += 1
                self.running += len(result.next_urls)

        print("Terminating...")
