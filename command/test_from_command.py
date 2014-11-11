import logging, unittest, sys
from optparse import OptionParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ConfigParser import SafeConfigParser


USERNAME = "wangxinhui1213"
ACCESS_KEY = "e63575e6-8d6d-4a09-80df-2d4e7f4b5c4d"
 
class Selenium2OnSauce(unittest.TestCase):
    "Example class written to run Selenium tests on Sauce Labs"
    def __init__(self,config_file,test_run):
        "Constructor: Accepts the configuration file and the test run name as parameters"
        self.config_file = config_file
        self.test_run = test_run
 
    def setUp(self):
        "Setup for this test involves spinning up the right virtual machine on Sauce Labs"
        parser = SafeConfigParser()
        parser.read(self.config_file)
 
        if parser.get(self.test_run, 'browser').lower()=='chrome':
            desired_capabilities = webdriver.DesiredCapabilities.CHROME
        if parser.get(self.test_run, 'browser').lower()in ['firefox','ff']:
            desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        if parser.get(self.test_run, 'browser').lower()in ['internet explorer','ie']:
            desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
 
        desired_capabilities['version'] = parser.get(self.test_run, 'version')
        desired_capabilities['platform'] = parser.get(self.test_run, 'platform')
        desired_capabilities['name'] = parser.get(self.test_run, 'name')
        desired_capabilities['build'] = parser.get(self.test_run, 'build')
        desired_capabilities['tags'] = parser.get(self.test_run, 'tag')
        desired_capabilities['record-video'] = parser.get(self.test_run, 'record-video')
        desired_capabilities['video-upload-on-pass'] = parser.get(self.test_run, 'video-upload-on-pass')
        desired_capabilities['record-screenshots'] = parser.get(self.test_run, 'record-screenshots')
 
        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (USERNAME, ACCESS_KEY)
        )
        self.driver.implicitly_wait(30)
 
 
    def test_search_in_python_org(self):
        "An example test: Visit python.org and search for BeautifulSoup"
        #Go to the URL 
        self.driver.get("http://www.python.org")
 
        #Assert that the title is correct
        self.assertIn("Python", self.driver.title)
 
        #Identify the xpath and send the string you want
        elem = self.driver.find_element_by_xpath("//input[@id='id-search-field']")
        print "About to search for the string BeautifulSoup on python.org"
        elem.send_keys("BeautifulSoup")
        elem.send_keys(Keys.RETURN)
        print "Search for the string BeautifulSoup on python.org was successful"
 
 
    def tearDown(self):
        "Finish the test run"
        self.driver.quit()
 
 
#---START OF SCRIPT
if __name__ == '__main__':
    #Lets accept some command line options from the user
    #We have chosen to use the Python module optparse 
    usage = "usage: %prog -c  -t  \nE.g.1: %prog -c ./test_configuration.ini -t \"Nightly Run\"\n---"
    parser = OptionParser(usage=usage)
    parser.add_option("-c","--config",dest="config_file",help="The full path of the configuration file")
    parser.add_option("-t","--test_run",dest="test_run",help="The name of the test run")
    (options,args) = parser.parse_args()
 
    #Create a test obj with our parameters
    test_obj = Selenium2OnSauce(config_file=options.config_file,test_run=options.test_run)
 
    #We are explicitly calling setup snd tearDown because what we are showing is technically not a unit test
    test_obj.setUp()
 
    #Run the test itself. NOTE: This is NOT a unit test
    test_obj.test_search_in_python_org()
 
    #We are explicitly calling setup snd tearDown because what we are showing is technically not a unit test
    test_obj.tearDown()
