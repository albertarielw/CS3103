from HTTP import Get
from HTMLParser import HTMLParser
from enum import Enum
from dataclasses import dataclass

class Analysis():
    def __init__(self, input):
        self.input = self._parseInput(input)

        self.analysisJobType = self._generateMapping(JobTypeMapping.MAPPING.value)

    def _parseInput(self, input):
        return input.lower().replace(" ", "").replace("\n", "")

    def _generateMapping(self, typeMapping: dict):
        map = {}
        for key in typeMapping.keys():
            map[key] = 0
        return map

    def _analyse(self, analysis:dict, typeMapping: dict):
        for type in analysis:
            isKeywordPresent = False
            for keyword in typeMapping[type]:
                if keyword in self.input:
                    isKeywordPresent = True
                    break
            
            if isKeywordPresent:
                analysis[type] += 1

    def printAnalysis(self):
        print(self.analysisJobType)

class JobType(Enum):
    FULLTIME = "FULLTIME"
    PARTTIME = "PARTIME"
    BOTH = "BOTH"

    FULLTIME_KEYWORDS = ("full time", "fulltime", "full-time")
    PARTTIME_KEYWORDS = ("part time", "parttime", "part-time")

class JobTypeMapping(Enum):
    MAPPING = {JobType.FULLTIME: JobType.FULLTIME_KEYWORDS, JobType.PARTTIME: JobType.FULLTIME_KEYWORDS}

### TEST ###

text = Get("https://jobs.polymer.co/whalesync/28574")
htmlParser = HTMLParser(text)

soup = htmlParser.GetSoup()
text = soup.get_text()

analysis = Analysis(text)
# # print(analysis.input)

# analysis.analyseJobType()
# analysis.printAnalysis()

