from HTTP import Get
from HTMLParser import HTMLParser
from enum import Enum
from abc import ABC, abstractmethod
import re

class KeywordAnalysis():
    def __init__(self, mapping):
        self.mapping = mapping
        self.analysis = self._setupAnalysis()
        
    def _setupAnalysis(self):
        initial_analysis = {}
        for key in self.mapping.value.keys():
            initial_analysis[key] = 0
        return initial_analysis

    def runAnalysis(self, input):
        for key, keywords in self.mapping.value.items():
            if type(keywords) == type(""):
                if keywords in input:
                    self.analysis[key] = 1
                    break
            else:
                for keyword in keywords:
                    if keyword in input:
                        self.analysis[key] = 1
                        break

class KeywordAnalysisKeyEnum(Enum):
    JOBTYPE = "JOB_TYPE"
    JOBLEVEL = "JOB_LEVEL"
    REQUIREDDEGREE = "REQUIRED_DEGREE"
    JOBROLE = "JOB_ROLE"
    TECHSKILL = "TECH_SKILL"

class JobTypeEnum(Enum):
    FULLTIME = "Full Time"
    PARTTIME = "Part Time"

    FULLTIME_KEYWORDS = ("full time", "fulltime", "full-time")
    PARTTIME_KEYWORDS = ("part time", "parttime", "part-time")

    MAPPING = {FULLTIME: FULLTIME_KEYWORDS, PARTTIME: PARTTIME_KEYWORDS}

class JobLevelEnum(Enum):
    INTERN = "Internship"
    JUNIOR = "Junior"
    SENIOR = "Senior"
    EXECUTIVE = "Executive"

    INTERN_KEYWORDS = ("intern")
    JUNIOR_KEYWORDS = ("junior", "jr", "entry")
    SENIOR_KEYWORDS = ("senior", "sr", "experienced")
    EXECUTIVE_KEYWORDS = ("executive", "chief", "cto")

    MAPPING = {INTERN: INTERN_KEYWORDS, JUNIOR: JUNIOR_KEYWORDS, SENIOR: SENIOR_KEYWORDS, EXECUTIVE: EXECUTIVE_KEYWORDS}

class RequiredDegreeEnum(Enum):
    NONE_REQUIRED = "None"
    BACHELOR = "Bachelor"
    GRADUATE = "Graduate"
    MASTER = "MASTER"
    PHD = "PHD"

    NONE_KEYWORDS = ("nodegree")
    BACHELOR_KEYWORDS = ("bachelor", "ongoing", "currentstudent")
    GRADUATE_KEYWORDS = ("graduate", "graduated")
    MASTER_KEYWORDS = ("master")
    PHD_KEYWORDS = ("phd", "doctorate", "doctorofphilosophy")

    MAPPING = {NONE_REQUIRED: NONE_KEYWORDS, BACHELOR: BACHELOR_KEYWORDS, GRADUATE: GRADUATE_KEYWORDS, MASTER: MASTER_KEYWORDS, PHD: PHD_KEYWORDS}

class JobRoleEnum(Enum):
    SOFTWARE_ENGINEER = "SoftEng"
    QUALITY_ASSURANCE = "QA"
    DATA_SCIENTIST = "DS"
    WEB_DEVELOPER = "WebDev"
    FRONT_END = "Front End"
    BACK_END = "Back End"
    FULLSTACK = "Fullstack"
    RESEARCH = "Research"
    NETWORKING = "Networking"
    TEST_ENGINEER = "Test Engineer"
    ML_ENGINEER = "ML"
    AI_ENGINEER = "AI"

    SE_KEYWORDS = ("softeng", "softwareengineer", "softwaredeveloper")
    QA_KEYWORDS = ("qa", "qualityassurance")
    DS_KEYWORDS = ("dataengineer", "dataanalyst")
    WEBDEV_KEYWORDS = ("webdeveloper", "website", "webdev")
    FRONTEND_KEYWORDS = ("frontend", "front-end")
    BACKEND_KEYWORDS = ("backend", "back-end")
    FULLSTACK_KEYWORDS = ("fullstack")
    RESEARCH_KEYWORDS = ("research", "r&d", "rnd")
    NETWORKING_KEYWORDS = ("networking", "tcp", "ip", "protocol", "http")
    TESTING_KEYWORDS = ("testing", "testcase", "test")
    ML_KEYWORDS = ("machinelearning", "ml")
    AI_KEYWORDS = ("artificialintelligence", "ai")

    MAPPING = {SOFTWARE_ENGINEER: SE_KEYWORDS, QUALITY_ASSURANCE: QA_KEYWORDS, DATA_SCIENTIST: DS_KEYWORDS, WEB_DEVELOPER: WEBDEV_KEYWORDS, FRONT_END: FRONTEND_KEYWORDS, BACK_END: BACKEND_KEYWORDS, FULLSTACK: FULLSTACK_KEYWORDS, RESEARCH: RESEARCH_KEYWORDS, NETWORKING: NETWORKING_KEYWORDS, TEST_ENGINEER: TESTING_KEYWORDS, ML_ENGINEER: ML_KEYWORDS, AI_ENGINEER: AI_KEYWORDS}

class TechSkillEnum(Enum):
    JAVA = "Java"
    JAVASCRIPT = "JS"
    CPP = "CPP"
    PYTHON = "Python"
    SQL = "SQL"
    RUBY = "Ruby"
    PHP = "PHP"
    LINUX = "Linux"
    FIGMA = "Figma"
    NUMPY = "Numpy"
    PYTORCH = "Pytorch"
    REACTJS = "React"
    VIM = "VIM"
    ASSEMBLY = "Assembly"
    CSS = "css"

    JAVA_KEYWORDS = ("java")
    JS_KEYWORDS = ("js", "javascript")
    CPP_KEYWORDS = ("c++", "cpp")
    PYTHON_KEYWORDS = ("python")
    SQL_KEYWORDS = ("sql")
    RUBY_KEYWORDS = ("ruby")
    PHP_KEYWORDS = ("php")
    LINUX_KEYWORDS = ("linux")
    FIGMA_KEYWORDS = ("figma")
    NUMPY_KEYWORDS = ("numpy")
    PYTORCH_KEYWORDS = ("pytorch")
    REACT_KEYWORDS = ("react", "react.js")
    VIM_KEYWORDS = ("vim")
    ASSEMBLY_KEYWORDS = ("assembly")
    CSS_KEYWORDS = ("css")

    MAPPING = {JAVA: JAVA_KEYWORDS, JAVASCRIPT: JS_KEYWORDS, CPP: CPP_KEYWORDS, PYTHON: PYTHON_KEYWORDS, SQL: SQL_KEYWORDS, RUBY: RUBY_KEYWORDS, PHP: PHP_KEYWORDS, LINUX: LINUX_KEYWORDS, FIGMA: FIGMA_KEYWORDS, NUMPY: NUMPY_KEYWORDS, PYTORCH: PYTHON_KEYWORDS, REACTJS: REACT_KEYWORDS, VIM: VIM_KEYWORDS, ASSEMBLY: ASSEMBLY_KEYWORDS, CSS: CSS_KEYWORDS}

class Analysis():
    def __init__(self, input):
        self.input = self.parseInput(input)
        self.keywordAnalysis = self._runKeywordAnalysis()
        self.salary = None

    def parseInput(self, input):
        return input.lower().replace("\n", " ")

    def _runKeywordAnalysis(self):
        result = {}

        mapping = {}
        mapping[KeywordAnalysisKeyEnum.JOBTYPE] = KeywordAnalysis(JobTypeEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.JOBLEVEL] = KeywordAnalysis(JobLevelEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.REQUIREDDEGREE] = KeywordAnalysis(RequiredDegreeEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.JOBROLE] = KeywordAnalysis(JobRoleEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.TECHSKILL] = KeywordAnalysis(TechSkillEnum.MAPPING)

        for key, value in mapping.items():
            value.runAnalysis(self.input)
            result[key.value] = value.analysis
        self.salary = re.findall("\$\d+(?:,\d+)*(?:\.\d+)?[KMkkmMm]?|-?\$\d+(?:,\d+)*(?:-\d+)?[KMkkmMm]?",text)
        print(self.salary)

        return result
    
    def printKeywordAnalysis(self):
        print(self.keywordAnalysis)


### TEST ###

text = Get("https://jobs.polymer.co/whalesync/28574")
htmlParser = HTMLParser(text)

soup = htmlParser.GetSoup()
text = soup.get_text()

analysis = Analysis(text)
analysis.printKeywordAnalysis()
