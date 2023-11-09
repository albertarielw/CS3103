import socket
from urllib import parse
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
from HTTP import Get
from HTMLParser import HTMLParser
from collections import deque
from Taskmanager import TaskResult
from typing import Optional
from Analysis import Analysis
import time


class Webcrawler:
    def crawl(self, url: str) -> Optional[TaskResult]:
        """
        crawl crawls the given url and returns a TaskResult.
        """
        print("crawling: ", url)

        html = ""
        try:
            # record time
            start_time = time.time()
            html = Get(url)
            end_time = time.time()
        except Exception as e:
            print("Error in Get:", e)
            return None

        # parse html response
        parser = HTMLParser(html)
        next_urls = parser.GetLinks()

        # analyze html response
        soup = parser.GetSoup()
        analysis = Analysis(soup.get_text())
        ip_addr = self.get_ip_addr(url)
        address_info = DbIpCity.get(ip_addr, api_key="free")

        return TaskResult(
            url=url,
            ip_addr=address_info.ip_address,
            geolocation=f"{address_info.city}, {address_info.region}, {address_info.country}",
            next_urls=next_urls,
            rtt=round(end_time - start_time, 3),
            analysis=analysis,
        )

    def get_ip_addr(self, url: str) -> str:
        """
        get_ip_addr returns the IP address for the given url.
        """
        return socket.gethostbyname(parse.urlparse(url).hostname)
