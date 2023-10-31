from HTTP import Get
from HTMLParser import HTMLParser

class Analysis():
    def __init__(self, input):
        self.input = self.parseInput(input)

        self.analysisJobType = {}

    def parseInput(self, input):
        return input.lower().replace(" ", "").replace("\n", "")

    def analyzeJobType(self):
        pass

    def print(self):
        print(self.input)





text = Get("https://jobs.polymer.co/whalesync/28574")
htmlParser = HTMLParser(text)

soup = htmlParser.GetSoup()
text = soup.get_text()

analysis = Analysis(text)
analysis.print()