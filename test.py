#!/usr/bin/python
# _*_ coding: utf-8 _*_

import logging, unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
USERNAME = "wangxinhui1213"
ACCESS_KEY = "e63575e6-8d6d-4a09-80df-2d4e7f4b5c4d"
 
class Selenium2OnSauce(unittest.TestCase):
 
    def setUp(self):
        #self.driver = webdriver.Firefox()
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX 
        desired_capabilities['version'] = '24'
        desired_capabilities['platform'] = 'Windows 7'
        desired_capabilities['name'] = 'Testing Search functionality in Python website using Python at Sauce'
 
        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            #command_executor="http://$USERNAME:$ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub"
            command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (USERNAME, ACCESS_KEY)
        )
        self.driver.implicitly_wait(30)
 
    def test_search_in_python_org(self):
        #Go to the URL 
        self.driver.get("http://www.python.org")
 
        #Assert that the title is correct
        self.assertIn("Python", self.driver.title)
 
        #Identify the xpath and send the string you want
        elem = self.driver.find_element_by_xpath("//input[@id='id-search-field']")
        print "About to search for the string BeautifulSoup on python.org"
        elem.send_keys("BeautifulSoup")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main()
