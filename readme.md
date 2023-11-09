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

#### Running the web crawler script 

To start the web crawler, run the following command 

```bash 
python main.py
```

The script will start retrieving pages from the URLs and the result in the form of `id::url;;ip_address;;ip_address_geolocation;;response_time` will be added into `database.txt`. Additionally, a json file named `analysis.json` will be created that contains keyword analysis of the html files found so far.

#### Running analysis visualisation

To run the dashboard for analysis visualisation, run the following command

```bash 
streamlit run Dashboard.py
```

Note:
- This command is for macOS, for other environments please refer to [https://docs.streamlit.io/library/get-started](https://docs.streamlit.io/library/get-started)
- If you have not run the web crawler script (and thus `analysis.json` is not created yet), data will be loaded from `sample.json`
- Sample visualisation is provided in: [charts.pdf](./charts.pdf)


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

#### Analysis 

The analysis process is designed to explore and quantify the prominence of various aspects related to job postings within the Computer Science industry, such as job roles, job modes, programming language, technology framework and many more. To achieve this, the code conducts keyword analysis for each job posting page, systematically examining the presence of specific keywords associated with these attributes. For example, in the context of job roles, a set of keywords is defined for each job role, and if any of these keywords are found on a job posting page, it's considered as a mention of that job role. The accumulation of these mentions is done across a sample of web crawled pages, enabling the determination of the relative popularity of different job roles and other categories. After each analysis, the result file is updated using a mutex to prevent data race, ensuring the integrity and consistency of the collected data. This approach provides valuable insights into which job attributes are most frequently mentioned in job postings, helping to identify trends and patterns in the Computer Science job market.

#### Dashboard for Analysis Visualisation

The visualization process is designed to present data obtained from the analysis of HTML pages acquired through web crawling. It reads the `analysis.json` file, which contains aggregated data resulting from keyword analysis, and generates bar and pie charts using the Streamlit and Matplotlib libraries. For clarity and ease of comprehension, categories with fewer than 9 values are represented as pie charts, while categories with 9 or more values are visualized as bar charts, displaying only the top 9 values. This visualization process aims to enhance the reader's understanding of the data and improve the report's overall clarity. The decision to display only the top 9 values in the visualization is based on considerations of relevance, clarity, visual impact, and focus, ensuring that the audience can better discern the most significant data points, thereby aiding in the extraction of meaningful insights from the data presentation.

## Contributors 

- Albert Ariel W. 
- Daffa Fathani A. 
- Kevin Nathanael M. 
- Stevan Gerard G. 