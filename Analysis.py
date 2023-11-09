from HTTP import Get
from HTMLParser import HTMLParser
from enum import Enum
from typing import Dict
import json

class Analysis():
    def __init__(self, inp):
        """
        Initializes an Analysis instance with input data and keyword analysis results.

        Args:
            inp (str): The input data for analysis.
        """
        self.input = self._parseInput(inp)
        self.keywordAnalysis = self._runKeywordAnalysis()

    def _parseInput(self, inp):
        """
        Cleans and normalizes the input data by converting it to lowercase and replacing newline characters.

        Args:
            inp (str): The input data to be cleaned.

        Returns:
            str: The cleaned and normalized input data.
        """
        return inp.lower().replace("\n", " ")

    def _runKeywordAnalysis(self):
        """
        Runs keyword analysis on the cleaned input data for various categories and returns the results.

        Returns:
            dict: A dictionary containing keyword analysis results for different categories.
        """
        result = {}

        # Define a mapping of keyword analysis categories to their respective enums.
        mapping = {}
        mapping[KeywordAnalysisKeyEnum.JOB_TYPE] = KeywordAnalysis(JobTypeEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.JOB_LEVEL] = KeywordAnalysis(JobLevelEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.REQUIRED_DEGREE] = KeywordAnalysis(RequiredDegreeEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.JOB_MODE] = KeywordAnalysis(JobModeEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.JOB_ROLE] = KeywordAnalysis(JobRoleEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.COMMUNICATION] = KeywordAnalysis(CommunicationSkillEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.PROGRAMMING_LANGUAGE] = KeywordAnalysis(ProgrammingLanguageEnum.MAPPING)
        mapping[KeywordAnalysisKeyEnum.FRAMEWORK] = KeywordAnalysis(FrameworkEnum.MAPPING)

        # Run keyword analysis for each category and store the results in the 'result' dictionary.
        for key, value in mapping.items():
            value.runAnalysis(self.input)
            result[key.value] = value.analysis

        return result
    
    def printKeywordAnalysis(self):
        """
        Prints the keyword analysis results to the console.
        """
        print(self.keywordAnalysis)
    
class AnalysisManager:
    """
    A wrapper around the Analysis class. Used to accumulate Analysis objects and manage their data.
    """
    def __init__(self): 
        """
        Initializes an AnalysisManager instance with an empty Analysis object.
        """
        self.acc = Analysis("")
    
    def _merge_dict(self, d1, d2) -> Dict:
        """
        Merges two dictionaries by adding values of common keys and returns the merged dictionary.

        Args:
            d1 (dict): The first dictionary to merge.
            d2 (dict): The second dictionary to merge.

        Returns:
            dict: The merged dictionary with values summed for common keys.
        """
        return {key: (d1[key] + d2[key]) for key in d1}

    def add(self, analysis: Analysis) -> None:
        """
        Adds the keyword analysis results from another Analysis object to the accumulated Analysis object.

        Args:
            analysis (Analysis): The Analysis object to add.
        """
        result = {}
        dct1, dct2 = self.acc.keywordAnalysis, analysis.keywordAnalysis
        for key, val in dct1.items():
            result[key] = self._merge_dict(val, dct2[key])
        self.acc.keywordAnalysis = result
    
    def load(self, path: str) -> None: 
        """
        Loads keyword analysis data from a file and updates the accumulated Analysis object.

        Args:
            path (str): The path to the file containing the keyword analysis data (in JSON format).
        """
        with open(path, 'r') as f:
            self.acc.keywordAnalysis = json.load(f) 

    def store(self, path: str) -> None: 
        """
        Stores the accumulated keyword analysis data to a file in JSON format.

        Args:
            path (str): The path to the file where the data will be stored.
        """
        with open(path, 'w') as f:
            json.dump(self.acc.keywordAnalysis, f, indent=4)
        
class KeywordAnalysis():
    """
    Performs keyword analysis for a specific category based on provided mappings.
    """
    def __init__(self, mapping):
        """
        Initializes a KeywordAnalysis instance with a mapping for the category.

        Args:
            mapping (MappingEnum): The mapping for the category.
        """
        self.mapping = mapping
        self.analysis = self._setupAnalysis()
        
    def _setupAnalysis(self):
        """
        Sets up the initial analysis results as a dictionary with keys from the mapping and initial values set to 0.

        Returns:
            dict: The initial analysis results for the category.
        """
        initial_analysis = {}
        for key in self.mapping.value.keys():
            initial_analysis[key] = 0
        return initial_analysis

    def runAnalysis(self, input):
        """
        Performs keyword analysis on the input data for the category and updates the analysis results.

        Args:
            input (str): The input data for analysis.
        """
        for key, keywords in self.mapping.value.items():
            if type(keywords) == type(""):
                if keywords in input:
                    self.analysis[key] = 1
                    continue
            else:
                for keyword in keywords:
                    if keyword in input:
                        self.analysis[key] = 1
                        break

class KeywordAnalysisKeyEnum(Enum):
    """
    Enum representing the possible keys for keyword analysis categories.
    """
    JOB_TYPE = "JOB_TYPE"
    JOB_LEVEL = "JOB_LEVEL"
    REQUIRED_DEGREE = "REQUIRED_DEGREE"
    JOB_MODE = "JOB_MODE"
    JOB_ROLE = "JOB_ROLE"
    COMMUNICATION = "COMMUNICATION"
    PROGRAMMING_LANGUAGE = "PROGRAMMING_LANGUAGE"
    FRAMEWORK = "FRAMEWORK"

class JobTypeEnum(Enum):
    """
    Enum representing job types along with their associated keywords for analysis.
    """
    FULLTIME = "Full Time"
    PARTTIME = "Part Time"

    FULLTIME_KEYWORDS = ("full time", "fulltime", "full-time")
    PARTTIME_KEYWORDS = ("part time", "parttime", "part-time")

    MAPPING = {FULLTIME: FULLTIME_KEYWORDS, PARTTIME: PARTTIME_KEYWORDS}

class JobLevelEnum(Enum):
    """
    Enum representing job levels along with their associated keywords for analysis.
    """
    INTERN = "Intern"
    JUNIOR = "Junior"
    SENIOR = "Senior"
    EXECUTIVE = "Executive"

    INTERN_KEYWORDS = ("intern")
    JUNIOR_KEYWORDS = ("junior", "jr", "entry")
    SENIOR_KEYWORDS = ("senior", "sr", "experienced")
    EXECUTIVE_KEYWORDS = ("executive", "chief", "cto")

    MAPPING = {INTERN: INTERN_KEYWORDS, JUNIOR: JUNIOR_KEYWORDS, SENIOR: SENIOR_KEYWORDS, EXECUTIVE: EXECUTIVE_KEYWORDS}

class RequiredDegreeEnum(Enum):
    """
    Enum representing required degree types along with their associated keywords for analysis.
    """
    NONE_REQUIRED = "None"
    BACHELOR = "Bachelor"
    GRADUATE = "Graduate"
    MASTER = "MASTER"
    PHD = "PHD"

    NONE_KEYWORDS = ("nodegree", "no degree")
    BACHELOR_KEYWORDS = ("bachelor", "ongoing", "currentstudent", "current student")
    GRADUATE_KEYWORDS = ("graduate", "graduated")
    MASTER_KEYWORDS = ("master")
    PHD_KEYWORDS = ("phd", "doctorate", "doctorofphilosophy", "doctor of philosophy")

    MAPPING = {NONE_REQUIRED: NONE_KEYWORDS, BACHELOR: BACHELOR_KEYWORDS, GRADUATE: GRADUATE_KEYWORDS, MASTER: MASTER_KEYWORDS, PHD: PHD_KEYWORDS}

class JobModeEnum(Enum):
    """
    Enum representing job modes along with their associated keywords for analysis.
    """
    ONSITE = "On-Site"
    REMOTE = "Remote"
    HYBRID = "Hybrid"

    ONSITE_KEYWORDS = ("onsite", "on-site", "in-office", "in office")
    REMOTE_KEYWORDS = ("remote", "work from home", "telecommute")
    HYBRID_KEYWORDS = ("hybrid", "on-site and remote", "on-site or remote", "onsite and remote", "onsite or remote")

    MAPPING = {
        ONSITE: ONSITE_KEYWORDS,
        REMOTE: REMOTE_KEYWORDS,
        HYBRID: HYBRID_KEYWORDS,
    }

class JobRoleEnum(Enum):
    """
    Enum representing job roles along with their associated keywords for analysis.
    """
    SOFTWARE_ENGINEER = "Software Engineer"
    QUALITY_ASSURANCE = "Quality Assurance"
    DATA_SCIENTIST = "Data Scientist"
    WEB_DEVELOPER = "Web Developer"
    FRONTEND = "Frontend Developer"
    BACKEND = "Backend Developer"
    FULLSTACK = "Full Stack Developer"
    RESEARCH = "Researcher"
    NETWORKING = "Networking Engineer"
    TEST_ENGINEER = "Test Engineer"
    ML_ENGINEER = "Machine Learning Engineer"
    AI_ENGINEER = "AI Engineer"
    DEVOPS = "DevOps Engineer"
    SYSTEM_ADMIN = "System Administrator"
    CLOUD_ARCHITECT = "Cloud Architect"
    DATABASE_ADMIN = "Database Administrator"
    SECURITY_ANALYST = "Security Analyst"
    MOBILE_APP_DEV = "Mobile App Developer"
    GAME_DEVELOPER = "Game Developer"
    UI_UX_DESIGNER = "UI/UX Designer"
    TECH_SUPPORT = "Technical Support"
    PRODUCT_MANAGER = "Product Manager"
    IT_MANAGER = "IT Manager"

    SOFTWARE_ENGINEER_KEYWORDS = ("softeng", "software")
    QUALITY_ASSURANCE_KEYWORDS = ("qa", "qualityassurance")
    DATA_SCIENTIST_KEYWORDS = ("datascientist", "dataanalyst")
    WEBDEV_KEYWORDS = ("webdeveloper", "webdev")
    FRONTEND_KEYWORDS = ("frontenddeveloper", "frontend")
    BACKEND_KEYWORDS = ("backenddeveloper", "backend")
    FULLSTACK_KEYWORDS = ("fullstackdeveloper", "fullstack", "full stack", "full-stack")
    RESEARCH_KEYWORDS = ("researcher", "research", "rnd")
    NETWORKING_KEYWORDS = ("networkingengineer", "networking", "networkengineer", "networks")
    TESTING_KEYWORDS = ("testengineer", "testing", "testcase", "test")
    ML_ENGINEER_KEYWORDS = ("machinelearningengineer", "machinelearning")
    AI_ENGINEER_KEYWORDS = ("aiengineer", "artificialintelligence")
    DEVOPS_KEYWORDS = ("devops", "devopsengineer")
    SYSTEM_ADMIN_KEYWORDS = ("systemadmin", "sysadmin")
    CLOUD_ARCHITECT_KEYWORDS = ("cloudarchitect", "cloud")
    DATABASE_ADMIN_KEYWORDS = ("dbadmin", "databaseadmin")
    SECURITY_ANALYST_KEYWORDS = ("securityanalyst", "cybersecurity")
    MOBILE_APP_DEV_KEYWORDS = ("mobileappdeveloper", "appdeveloper", "androiddev", "iosdev")
    GAME_DEVELOPER_KEYWORDS = ("gamedeveloper", "gameprogrammer", "gamedev")
    UI_UX_DESIGNER_KEYWORDS = ("uiuxdesigner", "uidesigner", "uxdesigner")
    TECH_SUPPORT_KEYWORDS = ("techsupport", "technicalsupport", "itsupport")
    PRODUCT_MANAGER_KEYWORDS = ("productmanager", "productowner")
    IT_MANAGER_KEYWORDS = ("itmanager", "itdirector")

    MAPPING = {
        SOFTWARE_ENGINEER: SOFTWARE_ENGINEER_KEYWORDS,
        QUALITY_ASSURANCE: QUALITY_ASSURANCE_KEYWORDS,
        DATA_SCIENTIST: DATA_SCIENTIST_KEYWORDS,
        WEB_DEVELOPER: WEBDEV_KEYWORDS,
        FRONTEND: FRONTEND_KEYWORDS,
        BACKEND: BACKEND_KEYWORDS,
        FULLSTACK: FULLSTACK_KEYWORDS,
        RESEARCH: RESEARCH_KEYWORDS,
        NETWORKING: NETWORKING_KEYWORDS,
        TEST_ENGINEER: TESTING_KEYWORDS,
        ML_ENGINEER: ML_ENGINEER_KEYWORDS,
        AI_ENGINEER: AI_ENGINEER_KEYWORDS,
        DEVOPS: DEVOPS_KEYWORDS,
        SYSTEM_ADMIN: SYSTEM_ADMIN_KEYWORDS,
        CLOUD_ARCHITECT: CLOUD_ARCHITECT_KEYWORDS,
        DATABASE_ADMIN: DATABASE_ADMIN_KEYWORDS,
        SECURITY_ANALYST: SECURITY_ANALYST_KEYWORDS,
        MOBILE_APP_DEV: MOBILE_APP_DEV_KEYWORDS,
        GAME_DEVELOPER: GAME_DEVELOPER_KEYWORDS,
        UI_UX_DESIGNER: UI_UX_DESIGNER_KEYWORDS,
        TECH_SUPPORT: TECH_SUPPORT_KEYWORDS,
        PRODUCT_MANAGER: PRODUCT_MANAGER_KEYWORDS,
        IT_MANAGER: IT_MANAGER_KEYWORDS,
    }

class CommunicationSkillEnum(Enum):
    """
    Enum representing communication skills along with their associated keywords for analysis.
    """
    COLLABORATION = "Collaboration"
    PRESENTATION = "Presentation"
    COMPETITIVE = "Competitive"
    TEAMWORK = "Teamwork"
    LEADERSHIP = "Leadership"
    CREATIVITY = "Creativity"
    CONFLICT_RESOLUTION = "Conflict Resolution"
    AMBITIOUS = "Ambitious"
    CRITICAL_THINKING = "Critical Thinking"
    TIME_MANAGEMENT = "Time Management"
    PROBLEM_SOLVING = "Problem Solving"
    ENTHUSIASM = "Enthusiasm"
    FEEDBACK_RECEPTIVITY = "Feedback Receptivity"
    ATTENTIVENESS = "Attentiveness"

    COLLABORATION_KEYWORDS = ("collaborative", "cooperative", "collaboration")
    PRESENTATION_KEYWORDS = ("presentation", "public speaking")
    COMPETITIVE_KEYWORDS = ("competitive", "competition")
    TEAMWORK_KEYWORDS = ("team", "teamplayer", "team player", "team work")
    LEADERSHIP_KEYWORDS = ("lead", "leadership", "leader")
    CREATIVITY_KEYWORDS = ("creative", "creativity")
    CONFLICT_RESOLUTION_KEYWORDS = ("conflict")
    AMBITIOUS_KEYWORDS = ("ambition", "ambitious")
    CRITICAL_THINKING_KEYWORDS = ("critical")
    TIME_MANAGEMENT_KEYWORDS = ("time", "prioritization", "prioritisation", "priority")
    PROBLEM_SOLVING_KEYWORDS = ("problem solving", "problemsolving", "problem-solving", "problem solv")
    ENTHUSIASM_KEYWORDS = ("enthu", "excited", "excitement")
    FEEDBACK_RECEPTIVITY_KEYWORDS = ("feedback", "criticism", "critique")
    ATTENTIVENESS_KEYWORDS = ("attention", "attentive")

    MAPPING = {
        COLLABORATION: COLLABORATION_KEYWORDS,
        PRESENTATION: PRESENTATION_KEYWORDS,
        COMPETITIVE: COLLABORATION_KEYWORDS,
        TEAMWORK: TEAMWORK_KEYWORDS,
        LEADERSHIP: LEADERSHIP_KEYWORDS,
        CREATIVITY: CREATIVITY_KEYWORDS,
        CONFLICT_RESOLUTION: CONFLICT_RESOLUTION_KEYWORDS,
        AMBITIOUS: AMBITIOUS_KEYWORDS,
        CRITICAL_THINKING: CRITICAL_THINKING_KEYWORDS,
        TIME_MANAGEMENT: TIME_MANAGEMENT_KEYWORDS,
        PROBLEM_SOLVING: PROBLEM_SOLVING_KEYWORDS,
        ENTHUSIASM: ENTHUSIASM_KEYWORDS,
        FEEDBACK_RECEPTIVITY: FEEDBACK_RECEPTIVITY_KEYWORDS,
        ATTENTIVENESS: ATTENTIVENESS_KEYWORDS
    }

class FrameworkEnum(Enum):
    """
    Enum representing tech frameworks along with their associated keywords for analysis.
    """
    REACT = "React"
    DJANGO = "Django"
    LARAVEL = "Laravel"
    SPRING_BOOT = "Spring Boot"
    VUE_JS = "Vue.js"
    EXPRESS_JS = "Express.js"
    NEXT_JS = "Next.js"
    NUXT_JS = "Nuxt.js"
    ASP_NET_CORE = "ASP.NET Core"
    RUBY_ON_RAILS = "Ruby on Rails"
    SVELTE = "Svelte"
    ANGULAR = "Angular"
    NEST_JS = "Nest.js"
    KOA_JS = "Koa.js"
    FLUTTER = "Flutter"
    REACT_NATIVE = "React Native"
    TENSORFLOW = "TensorFlow"
    PYTORCH = "PyTorch"
    PYSPARK = "PySpark"
    SCIKIT_LEARN = "Scikit-learn"
    KERAS = "Keras"
    FLASK = "Flask"
    FASTAPI = "FastAPI"
    PYRAMID = "Pyramid"
    CATALYST = "Catalyst"
    CAKEPHP = "CakePHP"
    YII = "Yii"
    CODEIGNITER = "CodeIgniter"
    SYMFONY = "Symfony"
    ZEND_FRAMEWORK = "Zend Framework"
    LARAVEL_MIX = "Laravel Mix"
    WEBPACK = "Webpack"
    PARCEL = "Parcel"
    JEST = "Jest"
    CYPRESS = "Cypress"
    MOCHA = "Mocha"
    ENZYME = "Enzyme"
    JASMINE = "Jasmine"
    JUNIT = "JUnit"
    RSPEC = "RSpec"
    CAPYBARA = "Capybara"
    CUCUMBER = "Cucumber"
    SELENIUM = "Selenium"
    APPIUM = "Appium"
    DOCKER = "Docker"
    KUBERNETES = "Kubernetes"
    TERRAFORM = "Terraform"
    ANSIBLE = "Ansible"
    CHEF = "Chef"
    PUPPET = "Puppet"

    # Define keywords for each framework
    REACT_KEYWORDS = ("react")
    DJANGO_KEYWORDS = ("django")
    LARAVEL_KEYWORDS = ("laravel")
    SPRING_BOOT_KEYWORDS = ("spring boot")
    VUE_JS_KEYWORDS = ("vue.js", "vuejs")
    EXPRESS_JS_KEYWORDS = ("express.js", "expressjs")
    NEXT_JS_KEYWORDS = ("next.js", "nextjs")
    NUXT_JS_KEYWORDS = ("nuxt.js", "nuxtjs")
    ASP_NET_CORE_KEYWORDS = ("asp.net core", "aspnet core")
    RUBY_ON_RAILS_KEYWORDS = ("ruby on rails", "rubyonrails")
    SVELTE_KEYWORDS = ("svelte")
    ANGULAR_KEYWORDS = ("angular")
    NEST_JS_KEYWORDS = ("nest.js", "nestjs")
    KOA_JS_KEYWORDS = ("koa.js", "koajs")
    FLUTTER_KEYWORDS = ("flutter")
    REACT_NATIVE_KEYWORDS = ("react native", "reactnative")
    TENSORFLOW_KEYWORDS = ("tensorflow")
    PYTORCH_KEYWORDS = ("pytorch")
    PYSPARK_KEYWORDS = ("pyspark")
    SCIKIT_LEARN_KEYWORDS = ("scikit-learn", "scikitlearn")
    KERAS_KEYWORDS = ("keras")
    FLASK_KEYWORDS = ("flask")
    FASTAPI_KEYWORDS = ("fastapi")
    PYRAMID_KEYWORDS = ("pyramid")
    CATALYST_KEYWORDS = ("catalyst")
    CAKEPHP_KEYWORDS = ("cakephp")
    YII_KEYWORDS = ("yii")
    CODEIGNITER_KEYWORDS = ("codeigniter")
    SYMFONY_KEYWORDS = ("symfony")
    ZEND_FRAMEWORK_KEYWORDS = ("zend framework", "zendframework")
    LARAVEL_MIX_KEYWORDS = ("laravel mix", "laravelmix")
    WEBPACK_KEYWORDS = ("webpack")
    PARCEL_KEYWORDS = ("parcel")
    JEST_KEYWORDS = ("jest")
    CYPRESS_KEYWORDS = ("cypress")
    MOCHA_KEYWORDS = ("mocha")
    ENZYME_KEYWORDS = ("enzyme")
    JASMINE_KEYWORDS = ("jasmine")
    JUNIT_KEYWORDS = ("junit")
    RSPEC_KEYWORDS = ("rspec")
    CAPYBARA_KEYWORDS = ("capybara")
    CUCUMBER_KEYWORDS = ("cucumber")
    SELENIUM_KEYWORDS = ("selenium")
    APPIUM_KEYWORDS = ("appium")
    DOCKER_KEYWORDS = ("docker")
    KUBERNETES_KEYWORDS = ("kubernetes")
    TERRAFORM_KEYWORDS = ("terraform")
    ANSIBLE_KEYWORDS = ("ansible")
    CHEF_KEYWORDS = ("chef")
    PUPPET_KEYWORDS = ("puppet")

    # Define a mapping of frameworks to their associated keywords
    MAPPING = {
        REACT: REACT_KEYWORDS,
        DJANGO: DJANGO_KEYWORDS,
        LARAVEL: LARAVEL_KEYWORDS,
        SPRING_BOOT: SPRING_BOOT_KEYWORDS,
        VUE_JS: VUE_JS_KEYWORDS,
        EXPRESS_JS: EXPRESS_JS_KEYWORDS,
        NEXT_JS: NEXT_JS_KEYWORDS,
        NUXT_JS: NUXT_JS_KEYWORDS,
        ASP_NET_CORE: ASP_NET_CORE_KEYWORDS,
        RUBY_ON_RAILS: RUBY_ON_RAILS_KEYWORDS,
        SVELTE: SVELTE_KEYWORDS,
        ANGULAR: ANGULAR_KEYWORDS,
        NEST_JS: NEST_JS_KEYWORDS,
        KOA_JS: KOA_JS_KEYWORDS,
        FLUTTER: FLUTTER_KEYWORDS,
        REACT_NATIVE: REACT_NATIVE_KEYWORDS,
        TENSORFLOW: TENSORFLOW_KEYWORDS,
        PYTORCH: PYTORCH_KEYWORDS,
        PYSPARK: PYSPARK_KEYWORDS,
        SCIKIT_LEARN: SCIKIT_LEARN_KEYWORDS,
        KERAS: KERAS_KEYWORDS,
        FLASK: FLASK_KEYWORDS,
        FASTAPI: FASTAPI_KEYWORDS,
        PYRAMID: PYRAMID_KEYWORDS,
        CATALYST: CATALYST_KEYWORDS,
        CAKEPHP: CAKEPHP_KEYWORDS,
        YII: YII_KEYWORDS,
        CODEIGNITER: CODEIGNITER_KEYWORDS,
        SYMFONY: SYMFONY_KEYWORDS,
        ZEND_FRAMEWORK: ZEND_FRAMEWORK_KEYWORDS,
        LARAVEL_MIX: LARAVEL_MIX_KEYWORDS,
        WEBPACK: WEBPACK_KEYWORDS,
        PARCEL: PARCEL_KEYWORDS,
        JEST: JEST_KEYWORDS,
        CYPRESS: CYPRESS_KEYWORDS,
        MOCHA: MOCHA_KEYWORDS,
        ENZYME: ENZYME_KEYWORDS,
        JASMINE: JASMINE_KEYWORDS,
        JUNIT: JUNIT_KEYWORDS,
        RSPEC: RSPEC_KEYWORDS,
        CAPYBARA: CAPYBARA_KEYWORDS,
        CUCUMBER: CUCUMBER_KEYWORDS,
        SELENIUM: SELENIUM_KEYWORDS,
        APPIUM: APPIUM_KEYWORDS,
        DOCKER: DOCKER_KEYWORDS,
        KUBERNETES: KUBERNETES_KEYWORDS,
        TERRAFORM: TERRAFORM_KEYWORDS,
        ANSIBLE: ANSIBLE_KEYWORDS,
        CHEF: CHEF_KEYWORDS,
        PUPPET: PUPPET_KEYWORDS,
    }

class ProgrammingLanguageEnum(Enum):
    """
    Enum representing programming languages along with their associated keywords for analysis.
    """
    JAVA = "Java"
    JAVASCRIPT = "JavaScript"
    CPP = "C++"
    PYTHON = "Python"
    SQL = "SQL"
    RUBY = "Ruby"
    PHP = "PHP"
    C_SHARP = "C#"
    SWIFT = "Swift"
    GO = "Go"
    PERL = "Perl"
    KOTLIN = "Kotlin"
    TYPESCRIPT = "TypeScript"
    HTML = "HTML"
    DART = "Dart"
    COBOL = "COBOL"
    FORTRAN = "Fortran"
    SCALA = "Scala"
    VHDL = "VHDL"
    LUA = "Lua"
    ELIXIR = "Elixir"
    MATLAB = "MATLAB"
    HASKELL = "Haskell"
    OBJECTIVE_C = "Objective-C"
    GROOVY = "Groovy"
    CRYSTAL = "Crystal"
    COFFEE_SCRIPT = "CoffeeScript"
    ERLANG = "Erlang"
    COQ = "Coq"
    RACKET = "Racket"
    F_SHARP = "F#"
    PERL_6 = "Perl 6"
    COOL = "Cool"
    SCHEME = "Scheme"
    PROLOG = "Prolog"
    ADA = "Ada"

    JAVA_KEYWORDS = ("java")
    JAVASCRIPT_KEYWORDS = ("js", "javascript")
    CPP_KEYWORDS = ("c++", "cpp")
    PYTHON_KEYWORDS = ("python")
    SQL_KEYWORDS = ("sql")
    RUBY_KEYWORDS = ("ruby")
    PHP_KEYWORDS = ("php")
    C_SHARP_KEYWORDS = ("c#", "csharp")
    SWIFT_KEYWORDS = ("swift")
    GO_KEYWORDS = ("golang")
    PERL_KEYWORDS = ("perl")
    KOTLIN_KEYWORDS = ("kotlin")
    TYPESCRIPT_KEYWORDS = ("typescript", "ts")
    HTML_KEYWORDS = ("html")
    DART_KEYWORDS = ("dart")
    COBOL_KEYWORDS = ("cobol")
    FORTRAN_KEYWORDS = ("fortran")
    SCALA_KEYWORDS = ("scala")
    VHDL_KEYWORDS = ("vhdl")
    LUA_KEYWORDS = ("lua")
    ELIXIR_KEYWORDS = ("elixir")
    MATLAB_KEYWORDS = ("matlab")
    HASKELL_KEYWORDS = ("haskell")
    OBJECTIVE_C_KEYWORDS = ("objective-c")
    GROOVY_KEYWORDS = ("groovy")
    CRYSTAL_KEYWORDS = ("crystal")
    COFFEE_SCRIPT_KEYWORDS = ("coffeescript")
    ERLANG_KEYWORDS = ("erlang")
    COQ_KEYWORDS = ("coq")
    RACKET_KEYWORDS = ("racket")
    F_SHARP_KEYWORDS = ("f#")
    PERL_6_KEYWORDS = ("perl 6")
    COOL_KEYWORDS = ("cool")
    SCHEME_KEYWORDS = ("scheme")
    PROLOG_KEYWORDS = ("prolog")
    ADA_KEYWORDS = ("ada")

    MAPPING = {
        JAVA: JAVA_KEYWORDS,
        JAVASCRIPT: JAVASCRIPT_KEYWORDS,
        CPP: CPP_KEYWORDS,
        PYTHON: PYTHON_KEYWORDS,
        SQL: SQL_KEYWORDS,
        RUBY: RUBY_KEYWORDS,
        PHP: PHP_KEYWORDS,
        C_SHARP: C_SHARP_KEYWORDS,
        SWIFT: SWIFT_KEYWORDS,
        GO: GO_KEYWORDS,
        PERL: PERL_KEYWORDS,
        KOTLIN: KOTLIN_KEYWORDS,
        TYPESCRIPT: TYPESCRIPT_KEYWORDS,
        HTML: HTML_KEYWORDS,
        DART: DART_KEYWORDS,
        COBOL: COBOL_KEYWORDS,
        FORTRAN: FORTRAN_KEYWORDS,
        SCALA: SCALA_KEYWORDS,
        VHDL: VHDL_KEYWORDS,
        LUA: LUA_KEYWORDS,
        ELIXIR: ELIXIR_KEYWORDS,
        MATLAB: MATLAB_KEYWORDS,
        HASKELL: HASKELL_KEYWORDS,
        SWIFT: SWIFT_KEYWORDS,
        OBJECTIVE_C: OBJECTIVE_C_KEYWORDS,
        GROOVY: GROOVY_KEYWORDS,
        CRYSTAL: CRYSTAL_KEYWORDS,
        COFFEE_SCRIPT: COFFEE_SCRIPT_KEYWORDS,
        ERLANG: ERLANG_KEYWORDS,
        COQ: COQ_KEYWORDS,
        COBOL: COBOL_KEYWORDS,
        RACKET: RACKET_KEYWORDS,
        F_SHARP: F_SHARP_KEYWORDS,
        PERL_6: PERL_6_KEYWORDS,
        COOL: COOL_KEYWORDS,
        SCHEME: SCHEME_KEYWORDS,
        PROLOG: PROLOG_KEYWORDS,
        ADA: ADA_KEYWORDS,
    }