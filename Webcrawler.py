import socket
from urllib import parse
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
from HTTP import Get
from HTMLParser import HTMLParser
from collections import deque
from Taskmanager import TaskResult
from typing import Optional
import time


class Webcrawler:
    def __init__(self):
        self.visited_urls = set()

    def crawl(self, url: str) -> Optional[TaskResult]:
        if url in self.visited_urls:
            print("visited, skiping: ", url)
            return None

        print("crawling: ", url)

        html = ""
        try:
            start_time = time.time()
            html = Get(url)
            end_time = time.time()
        except Exception as e:
            print("Error in Get:", e)
            return None

        myHTMLParser = HTMLParser(html)
        next_urls = myHTMLParser.GetLinks()

        soup = myHTMLParser.GetSoup()
        # analyze(soup)
        ip_addr = self.get_ip_addr(url)
        address_info = DbIpCity.get(ip_addr, api_key="free")
        self.visited_urls.add(url)
        return TaskResult(
            url=url,
            ip_addr=address_info.ip_address,
            geolocation=f"{address_info.city}, {address_info.region}, {address_info.country}",
            next_urls=next_urls,
            rtt=round(end_time-start_time, 3),
        )

    def get_ip_addr(self, url: str) -> str:
        return socket.gethostbyname(parse.urlparse(url).hostname)

    def analyze(self, soup):
        # TODO for stevan
        pass
