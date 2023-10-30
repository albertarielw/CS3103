from multiprocessing import Pool, Queue 
from typing import Callable, List
from functools import partial 
from dataclasses import dataclass
import time


@dataclass
class TaskResult: 
    """
    Wrapper for result returned by crawling function, e.g. 
    list of next urls, html file, time taken to process, etc. 
    """
    next_urls: List[str]
    html_file: str 
    rtt: float 

class TaskManager: 
    """
    Spawn a task pool to execute function specified in the constructor. 
    
    # Constructor argument and decorator is incomplete, 
    # function is expected to take a url string and Result Queue. 
    """
    def __init__(self, function: Callable[str, TaskResult], seed: list[str], timeout: float=10, num_procs:int=10):
        self.function = function 
        self.seed = seed 
        self.timeout = timeout 
        self.num_procs = num_procs 
        self.queue: Queue[TaskResult] = Queue()
        self.conn = None # TODO
        self.start_time = time.time()
    
    def timed_out(self) -> bool:
        """Check if timeout has been elapsed"""
        current_time = time.time()
        elapsed_time = current_time - self.start_time 
        return elapsed_time > self.timeout

    def start(self): 
        """
        Start a task pool, the master process will collect
        the result from queue and add more tasks to the pool
        """
        with Pool(self.num_procs) as task_pool:
            partial_func = partial(task_pool.apply_async, self.function, self.queue)
            
            # apply the partial function to all seed values, this call is async
            map(partial_func, self.seed) 
        
            while self.queue.not_empty: 
                # Check if it has timed out 
                if self.timed_out():
                    break 

                result = self.queue.get() 
                
                # TODO: Store the result
                self.conn.store(result)

                # Process next urls
                map(partial_func, result.next_urls) 
            
        print("Terminating...")



