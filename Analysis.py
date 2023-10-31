from HTTP import Get
from HTMLParser import HTMLParser
from enum import Enum

class Analysis():
    def __init__(self, input):
        self.input = self.parseInput(input)

        self.analysisJobRole = {JobRole.SOFTWARE_ENGINEER: 0, JobRole.QUALITY_ASSURANCE: 0, JobRole.DATA_SCIENTIST: 0, JobRole.WEB_DEVELOPER: 0, JobRole.FRONT_END: 0, JobRole.BACK_END: 0, JobRole.FULLSTACK: 0, JobRole.RESEARCH: 0, JobRole.NETWORKING: 0, JobRole.TEST_ENGINEER: 0, JobRole.ML_ENGINEER: 0, JobRole.AI_ENGINEER: 0}
        self.analysisRequiredDegree = {RequiredDegree.NONE_REQUIRED: 0, RequiredDegree.BACHELOR:0, RequiredDegree.GRADUATE:0, RequiredDegree.MASTER:0, RequiredDegree.PHD:0}
        self.analysisTechSkills = {TechSkill.JAVA: 0, TechSkill.JAVASCRIPT: 0, TechSkill.CPP: 0, TechSkill.PYTHON: 0, TechSkill.SQL: 0, TechSkill.RUBY: 0, TechSkill.PHP: 0, TechSkill.LINUX: 0, TechSkill.FIGMA: 0, TechSkill.NUMPY: 0, TechSkill.PYTORCH: 0, TechSkill.REACTJS: 0, TechSkill.VIM: 0, TechSkill.ASSEMBLY: 0, TechSkill.CSS: 0}
        self.jobSoftSkills = {"collaborative", "team_player", "independent", "can do", "proactive", "english", "mandarin", "problem solving", "adaptive", "leadership"}
        self.analysisJobLevel = {JobLevel.INTERN: 0, JobLevel.SENIOR: 0, JobLevel.JUNIOR: 0, JobLevel.EXECUTIVE: 0}
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
    
    
    def analyseJobLevel(self):
        isInternship = False
        for keyword in JobLevel.INTERNSHIP_KEYWORDS.value:
            if keyword in self.input:
                isInternship = True
                break
        
        isJunior = False
        for keyword in JobType.JUNIOR_KEYWORDS.value:
            if keyword in self.input:
                isJunior = True
                break

        isSenior = False
        for keyword in JobType.SENIOR_KEYWORDS.value:
            if keyword in self.input:
                isSenior = True
                break

        isExec = False
        for keyword in JobType.EXECUTIVE_KEYWORDS.value:
            if keyword in self.input:
                isExec = True
                break

        if isInternship:
            self.JobLevel[JobLevel.INTERN] = 1
            return
        
        if isJunior:
            self.JobLevel[JobLevel.JUNIOR] = 1
            return

        if isSenior:
            self.JobLevel[JobLevel.SENIOR] = 1
            return

        if isExec:
            self.JobLevel[JobLevel.EXECUTIVE] = 1
            return


    def analyseRequiredDegree(self):
        isBachelor = False
        for keyword in RequiredDegree.BACHELOR_KEYWORDS.value:
            if keyword in self.input:
                isBachelor = True
                break

        isMaster = False
        for keyword in RequiredDegree.MASTER_KEYWORDS.value:
            if keyword in self.input:
                isMaster = True
                break

        isPhd = False
        for keyword in RequiredDegree.PHD_KEYWORDS.value:
            if keyword in self.input:
                isPhd = True
                break

        isGraduate = isPhd or isMaster
        for keyword in RequiredDegree.GRADUATE_KEYWORDS.value:
            if keyword in self.input:
                isGraduate = True
                break

        isNoneRequired = not (isGraduate or isBachelor)
        for keyword in RequiredDegree.NONE_KEYWORDS.value:
            if keyword in self.input:
                isNoneRequired = True
                break

        if isNoneRequired:
            self.analysisRequiredDegree[DegreeRequired.NONE_REQUIRED] = 1
            return
        
        if isBachelor:
            self.analysisRequiredDegree[DegreeRequired.BACHELOR] = 1

        if isGraduate:
            self.analysisRequiredDegree[DegreeRequired.GRADUATE] = 1

        if isMaster:
            self.analysisRequiredDegree[DegreeRequired.MASTER] = 1
            
        if isPhd:
            self.analysisRequiredDegree[DegreeRequired.PHD] = 1
            
    def analyseJobRole(self):
        isSE = False
        for keyword in JobRole.SE_KEYWORDS.value:
            if keyword in self.input:
                isSE = True
                break

        isQA = False
        for keyword in JobRole.QA_KEYWORDS.value:
            if keyword in self.input:
                isQA = True
                break

        isDS = False
        for keyword in JobRole.DS_KEYWORDS.value:
            if keyword in self.input:
                isDS = True
                break

        isWebDev = False
        for keyword in JobRole.WEBDEV_KEYWORDS.value:
            if keyword in self.input:
                isGraduate = True
                break

        isFrontEnd = False
        for keyword in JobRole.FRONTEND_KEYWORDS.value:
            if keyword in self.input:
                isFrontEnd = True
                break
        
        isBackEnd = False
        for keyword in JobRole.BACKEND_KEYWORDS.value:
            if keyword in self.input:
                isBackEnd = True
                break
        
        isFullstack = False
        for keyword in JobRole.FULLSTACK_KEYWORDS.value:
            if keyword in self.input:
                isFullstack = True
                break
        
        isResearch = False
        for keyword in JobRole.RESEARCH_KEYWORDS.value:
            if keyword in self.input:
                isResearch = True
                break
        
        isNetworking = False
        for keyword in JobRole.NETWORKING_KEYWORDS.value:
            if keyword in self.input:
                isNetworking = True
                break
        
        isTesting = False
        for keyword in JobRole.TESTING_KEYWORDS.value:
            if keyword in self.input:
                isTesting = True
                break
        
        isML = False
        for keyword in JobRole.ML_KEYWORDS.value:
            if keyword in self.input:
                isML = True
                break
        
        isAI = False
        for keyword in JobRole.AI_KEYWORDS.value:
            if keyword in self.input:
                isAI = True
                break
        

        if isSE:
            self.analysisJobRole[JobRole.SOFTWARE_ENGINEER] = 1
            return
        
        if isQA:
            self.analysisJobRole[JobRole.QUALITY_ASSURANCE] = 1
            return

        if isDS:
            self.analysisJobRole[JobRole.DATA_SCIENTIST] = 1
            return

        if isWebDev:
            self.analysisJobRole[JobRole.WEB_DEVELOPER] = 1
            return
            
        if isFrontEnd:
            self.analysisJobRole[JobRole.FRONT_END] = 1
            return
        
        if isBackEnd:
            self.analysisJobRole[JobRole.BACK_END] = 1
            return
        
        if isFullstack:
            self.analysisJobRole[JobRole.FULLSTACK] = 1
            return
        
        if isResearch:
            self.analysisJobRole[JobRole.RESEARCH] = 1
            return

        if isTesting:
            self.analysisJobRole[JobRole.TEST_ENGINEER] = 1
            return

        if isML:
            self.analysisJobRole[JobRole.ML_ENGINEER] = 1
            return

        if isAI:
            self.analysisJobRole[JobRole.AI_ENGINEER] = 1
            return
        
        if isNetworking:
            self.analysisJobRole[JobRole.NETWORKING] = 1
            return
    
    def analyseJobRole(self):
        isJAVA = False
        for keyword in TechSkill.JAVA.value:
            if keyword in self.input:
                isJAVA = True
                break

        isJS = False
        for keyword in TechSkill.JAVASCRIPT.value:
            if keyword in self.input:
                isJS = True
                break

        isCPP = False
        for keyword in TechSkill.CPP.value:
            if keyword in self.input:
                isCPP = True
                break

        isPython = False
        for keyword in TechSkill.PYTHON.value:
            if keyword in self.input:
                isPython = True
                break

        isSQL = False
        for keyword in TechSkill.SQL.value:
            if keyword in self.input:
                isSQL = True
                break

        isRuby = False
        for keyword in TechSkill.RUBY.value:
            if keyword in self.input:
                isRuby = True
                break

        isPHP = False
        for keyword in TechSkill.PHP.value:
            if keyword in self.input:
                isPHP = True
                break

        isLINUX = False
        for keyword in TechSkill.LINUX.value:
            if keyword in self.input:
                isLInux = True
                break

        isFigma = False
        for keyword in TechSkill.FIGMA.value:
            if keyword in self.input:
                isFigma = True
                break

        isNumpy = False
        for keyword in TechSkill.NUMPY.value:
            if keyword in self.input:
                isNumpy = True
                break

        isPytorch = False
        for keyword in TechSkill.PYTORCH.value:
            if keyword in self.input:
                isPytorch = True
                break

        isReact = False
        for keyword in TechSkill.REACTJS.value:
            if keyword in self.input:
                isReact = True
                break

        isVIM = False
        for keyword in TechSkill.VIM.value:
            if keyword in self.input:
                isVIM = True
                break

        isAssembly = False
        for keyword in TechSkill.ASSEMBLY.value:
            if keyword in self.input:
                isAssembly = True
                break

        isCSS = False
        for keyword in TechSkill.CSS.value:
            if keyword in self.input:
                isCSS = True
                break


        if isJava:
            self.analysisTechSkills[TechSkill.JAVA] = 1
        
        if isJS:
            self.analysisTechSkills[TechSkill.JS] = 1
        
        if isCPP:
            self.analysisTechSkills[TechSkill.CPP] = 1
        
        if isPython:
            self.analysisTechSkills[TechSkill.PYTHON] = 1
        
        if isSQL:
            self.analysisTechSkills[TechSkill.SQL] = 1
        
        if isRuby:
            self.analysisTechSkills[TechSkill.RUBY] = 1
        
        if isPHP:
            self.analysisTechSkills[TechSkill.PHP] = 1
        
        if isLinux:
            self.analysisTechSkills[TechSkill.LINUX] = 1
        
        if isFigma:
            self.analysisTechSkills[TechSkill.FIGMA] = 1
        
        if isNumpy:
            self.analysisTechSkills[TechSkill.NUMPY] = 1
        
        if isPytorch:
            self.analysisTechSkills[TechSkill.PYTORCH] = 1
        
        if isReact:
            self.analysisTechSkills[TechSkill.REACTJS] = 1
        
        if isVIM:
            self.analysisTechSkills[TechSkill.VIM] = 1
        
        if isAssembly:
            self.analysisTechSkills[TechSkill.ASSEMBLY] = 1
        
        if isCSS:
            self.analysisTechSkills[TechSkill.CSS] = 1
        
        
        

        
    def print(self):
        print(self.input)

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

class JobLevel(Enum):
    INTERN = "Internships"
    SENIOR = "Senior"
    JUNIOR = "Junior"
    EXECUTIVE = "Executive"


    INTERNSHIP_KEYWORDS = ("intern", "internship")
    SENIOR_KEYWORDS = ("senior", "sr", "experienced")
    JUNIOR_KEYWORDS = ("junior", "jr", "entry")
    EXECUTIVE_KEYWORDS = ("executive", "chief", "cto")

class RequiredDegree(Enum):
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

class JobRole(Enum):
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


class TechSkill(Enum):
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

### TEST ###

text = Get("https://jobs.polymer.co/whalesync/28574")
htmlParser = HTMLParser(text)

soup = htmlParser.GetSoup()
text = soup.get_text()

analysis = Analysis(text)
# print(analysis.input)

analysis.analyseJobType()
analysis.printAnalysis()

