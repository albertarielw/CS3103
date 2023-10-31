from HTTP import Get
from HTMLParser import HTMLParser
from enum import Enum

class Analysis():
    def __init__(self, input):
        self.input = self.parseInput(input)

        self.analysisJobType = {JobType.FULLTIME: 0, JobType.PARTTIME: 0, JobType.BOTH: 0}

    def parseInput(self, input):
        return input.lower().replace(" ", "").replace("\n", "")

    def analyseJobType(self):
        isFullTime = False
        for keyword in JobType.FULLTIME_KEYWORDS.value:
            if keyword in self.input:
                isFullTime = True
                break
        
        isPartTime = False
        for keyword in JobType.PARTTIME_KEYWORDS.value:
            if keyword in self.input:
                isPartTime = True
                break

        if isFullTime and isPartTime:
            self.analysisJobType[JobType.BOTH] += 1
            return
        
        if isFullTime:
            self.analysisJobType[JobType.FULLTIME] += 1
            return

        if isPartTime:
            self.analysisJobType[JobType.PARTTIME] += 1
            return

    def printAnalysis(self):
        print(self.analysisJobType)

class JobType(Enum):
    FULLTIME = "FULLTIME"
    PARTTIME = "PARTIME"
    BOTH = "BOTH"

    FULLTIME_KEYWORDS = ("full time", "fulltime", "full-time")
    PARTTIME_KEYWORDS = ("part time", "parttime", "part-time")

### TEST ###

text = Get("https://jobs.polymer.co/whalesync/28574")
htmlParser = HTMLParser(text)

soup = htmlParser.GetSoup()
text = soup.get_text()

analysis = Analysis(text)
# print(analysis.input)

analysis.analyseJobType()
analysis.printAnalysis()

