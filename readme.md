# Parallel Web Crawler by Team 25

A web crawler (or web spider) is a program that retrieves and stores pages from the Web, commonly for a Web search engine (such as Google). A parallel crawler that runs multiple processes/threads in parallel. In this assignment you will implement a parallel web crawler using python, java, c++ that browses the WWW automatically by sending HTTP requests to many web servers in parallel. The crawler should start with a few web servers/web pages and should recursively discover more links (to more pages/servers).

## Project Setup
#### Setup Python

Make sure you have Python3 installed on your machine. You can download it from [python.org](https://www.python.org/).

```bash
# Verify your Python installation
python --version
```

#### Install Dependencies

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
# Install dependencies
pip install -r requirements.txt
```

## Running the Web Crawler Script 

#### Populating DB with seed values

Before running the script, the DB needs to be populated with initial URLs. To do this, create a file named `database.txt`, and populate the file with the following line and replace the    `<actual_url>` with the intended initial values of the URLs and `<id>` with the id of the entry. 

```
<id>::<actual_url>;;PENDING;;PENDING;;PENDING
```

example of initial state of `database.txt`:
```
0::https://news.ycombinator.com/jobs;;PENDING;;PENDING;;PENDING
1::https://news.ycombinator.com/jobs?next=37945432;;PENDING;;PENDING;;PENDING
```

#### Running the script 

To start the web crawler, run the following command 

```bash 
python main.py
```

The script will start retrieving pages from the URLs and the result in the form of `id::url;;ip_address;;ip_address_geolocation;;response_time` will be added into `database.txt`. Additionally, a json file named `analysis.json` will be created that contains keyword analysis of the html files found so far.

#### Configuring the web crawler 
To configure the crawler, go to `main.py` and change the following variables.

```python 
TIMEOUT = 600 # timeout in second until the crawler terminate 
NUM_PROCS = 10 # number of process spawned (excluding the main process)
NUM_URLS = 10000 # maximum number of urls to visit 
```



## Implementation Details 

#### Concurrency model 

We are using master-worker paradigm with Python's `Task Pool` [multiprocessing.Pool](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers) and `Synchronized Queue` [multiprocessing.Queue](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues). Initially, the master process (main process) spawns `num_procs` number of processes within the `Task Pool` and queue all the seed URLs to the `Task Pool`. Below are the steps followed to process a URL: 
- Master process sends the URL to the Task Pool. 
- Result returned by the worker process is sent back to the master process. This result contains all the necessary data such as ip address, ip geolocation, response time, analysis of the HTML page, as well as linked URLs from the page. 
- The result will be written to database.txt by the master process while the analysis will be aggregated with the analysis of other pages. 
- Linked URLs will be queued (again) to the Task Pool by the master process. 

#### Inter-process communication 

The worker processes need to send the result back to the master process and we are using message passing for communication between processes. Message passing allows us to avoid having to use synchronization primitives such as locks/mutexes. In this project, we are using Python's [multiprocessing.Queue](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues) that is multi-producer, multi-consumer FIFO queues, i.e. this queue implementation is already synchronized among processes. 

#### Coordinated write to DB 

The only process that have access to the DB is the master process. While the worker process are processing the URLs, the master process will write the result into the database.txt file. Hence, we are using implicit synchronization as we use Python's Synchonized Queue [multiprocessing.Queue](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues) that is shared among processes to send the result back to the master process. 



## Contributors 

- Albert Ariel W. 
- Daffa Fathani A. 
- Kevin Nathanael M. 
- Stevan Gerard G. 