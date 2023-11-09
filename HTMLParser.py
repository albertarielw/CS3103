import http.client
from bs4 import BeautifulSoup

class HTMLParser():
    def __init__(self, HTML):
        """
        Initialize the HTMLParser class with the provided HTML content.
        
        Args:
            HTML (str): The HTML content to be parsed.
        """
        self.HTML = HTML
        self.Soup = self._createSoup()

    def _createSoup(self):
        """
        Private method to create a BeautifulSoup object from the HTML content.

        Returns:
            BeautifulSoup: A BeautifulSoup object for parsing the HTML content.
        """
        soup = BeautifulSoup(self.HTML, 'html.parser')
        return soup
    
    def GetLinks(self):
        """
        Extract and return HTTP links (http:// and https://) from the HTML content.

        Returns:
            list: A list of HTTP links found in the HTML content.
        """
        links = self.Soup.find_all('a')

        result = []
        # Extract and print the HTTP links (http:// and https://)
        for link in links:
            href = link.get('href')
            if href and (href.startswith('http://') or href.startswith('https://')):
                result.append(href)
        
        return result
    
    def GetHTML(self):
        """
        Get the original HTML content.

        Returns:
            str: The original HTML content.
        """
        return self.HTML
    
    def GetSoup(self):
        """
        Get the BeautifulSoup object for parsed HTML.

        Returns:
            BeautifulSoup: A BeautifulSoup object for parsing the HTML content.
        """
        return self.Soup