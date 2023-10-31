import socket
from HTTP import Get
from HTMLParser import HTMLParser
from collections import deque
from Taskmanager import TaskResult
from typing import Optional


class Webcrawler:
    def __init__(self):
        self.visited_urls = set()

    def crawl(self, url: str) -> Optional[TaskResult]:
        if url in self.visited_urls:
            print("visited, skiping: ", url)
            return None

        print("crawling: ", url)

        HTML = ""
        try:
            HTML = Get(url)
        except Exception as e:
            print("Error in Get:", e)
            return None

        myHTMLParser = HTMLParser(HTML)
        next_urls = myHTMLParser.GetLinks()

        soup = myHTMLParser.GetSoup()
        # analyze(soup)
        print(self.get_ip_addr(url))
        self.visited_urls.add(url)
        return TaskResult(
            url=url,
            ip_addr="",
            geolocation="",
            next_urls=next_urls,
            rtt=1.0,
        )

    def get_ip_addr(self, url: str) -> str:
        return socket.gethostbyname(url)

    def analyze(self, soup):
        # TODO for stevan
        pass
