from HTTP import Get
from HTMLParser import HTMLParser

class Webcrawler():
    def __init__(self, URLToVisit):
        self.URLToVisit = set(URLToVisit)
        self.URLVisited = set()
        self.Analysis = {}

    def crawl(self, URL):
        if URL in self.URLVisited:
            return
        
        HTML = Get(URL)
        myHTMLParser = HTMLParser(HTML)
        links = myHTMLParser.GetLinks()
        for link in links:
            self.URLToVisit.add(link)
        
        soup = myHTMLParser.GetSoup()
        self.analyze(soup)

    
    def analyze(self, soup):
        # TODO for stevan
        pass


        