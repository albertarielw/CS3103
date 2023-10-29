import http.client
from bs4 import BeautifulSoup

class HTMLParser():
    def __init__(self, HTML):
        self.HTML = HTML
        self.Soup = self._createSoup()

    def _createSoup(self):
        soup = BeautifulSoup(self.HTML, 'html.parser')
        return soup
    
    def GetLinks(self):
        links = self.Soup.find_all('a')

        result = []
        # Extract and print the HTTP links (http:// and https://)
        for link in links:
            href = link.get('href')
            if href and (href.startswith('http://') or href.startswith('https://')):
                result.append(href)
        
        return result
    
    def GetHTML(self):
        return self.HTML
    
    def GetSoup(self):
        return self.Soup

# htmlParser = HTMLParser("www.example.com")
# print(htmlParser.GetLinks())