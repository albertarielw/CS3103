from HTTP import Get
from HTMLParser import HTMLParser

class Analysis():
    def __init__(self, input):
        self.input = self.parseInput(input)

        self.analysisJobType = {}
        self.analysisJobRole = {"software engineer" : 0, "qa" : 0, "data scientist":0, "web dev":0, "front end": 0, "back end":0, "fullstack":0, "research":0, "networking": 0, "test engineer" : 0, "ml" :0, "ai":0, "infrastructure"}
        self.jobDegree = {"none":0, "bachelors":0, "graduate":0, "master":0, "phd":0}
        self.jobSkills = {"java":0, "js":0}
        self.jobLevel = {"intern", "senior", "junior", "exec"}
    def parseInput(self, input):
        return input.lower().replace(" ", "").replace("\n", "")

    def analyzeJobType(self):
        pass

    def analyzeJobRole(self):
      isSoftEngRole = "softwareengineer" in self.input or "softwaredeveloper" in self.input or "softeng" in self.input
      isDataScientist = "datascientist" in self.input or 
      isWebDev = "webdeveloper" in self.input or 
      isFrontEnd = "frontend" in self.input or "front-end" in self.input
      isBackEnd = "backend" in self.input or "back-end" in self.input
      isFullStack = "fullstack" in self.input or "full-stack" in self.input
      isResearch = "researcher" in self.input or "research" in self.input
      isNetworking = "networkengineer" in self.input
      isTestEngineer = "testengineer" in self.input
      isAlgorithmEng = "algorithmengineer" in self.input
      isML = "machinelearning" in self.input or "machinelearningengineer" in self.input or "ml engineer" in self.input or "ml-engineer" in self.input or "ml" in input
      isAi = "artificialintelligenceengineer" in self.input or "ai" in self.input or "aiengineer" in self.input or "artificialintelligence" in self.input
      isInfrastructure = "infrastructureengineer" in self.input or "infrastructure" in self.input 
      isQualityAssurance = "qa" in self.input or "qualityassurance"

      if isSoftEngRole:
        self.analysisJobRole["software engineer"] = 1

    def print(self):
        print(self.input)





text = Get("https://jobs.polymer.co/whalesync/28574")
htmlParser = HTMLParser(text)

soup = htmlParser.GetSoup()
text = soup.get_text()

analysis = Analysis(text)
analysis.print()