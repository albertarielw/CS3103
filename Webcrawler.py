from HTTP import Get
from HTMLParser import HTMLParser
from collections import deque

class Webcrawler():
    def __init__(self, URLToVisit):
        self.URLToVisit = deque(URLToVisit) # change to queue?
        self.URLVisited = set()
        self.Analysis = {}

    def start(self):
        while len(self.URLToVisit) > 0:
            URL = self.URLToVisit.popleft()
            self.crawl(URL)

    def crawl(self, URL):
        print("crawling: ", URL)
        if URL in self.URLVisited:
            return
        
        HTML = ""
        try:
            HTML = Get(URL)
        except Exception as e:
            print("Error in Get:", e)
            return
        
        myHTMLParser = HTMLParser(HTML)
        links = myHTMLParser.GetLinks()
        for link in links:
            if link in self.URLVisited:
                continue
            self.URLToVisit.append(link)
        
        soup = myHTMLParser.GetSoup()
        self.analyze(soup)

    
    def analyze(self, soup):
        # TODO for stevan
        pass


URLToVisit = ["www.example.com"]
webcrawler = Webcrawler(URLToVisit=URLToVisit)
webcrawler.start()