#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest
import HTMLTestRunner

class PrmTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.111.113.26:8080/"
        self.username = "xinhuiwang"
        self.password = "welcome"
    
    def test_prm(self):
        driver = self.driver
        username = self.username
        password = self.password
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_id("login").click()

        welcome_info = driver.find_element_by_css_selector("#header_user > div").text
        self.assertEqual(welcome_info, "Welcome, " + username)

        driver.find_element_by_link_text("Admin").click()
        driver.find_element_by_id("ui-id-13").click()
        driver.find_element_by_css_selector("form.query_form > input[name=\"id\"]").clear()
        driver.find_element_by_css_selector("form.query_form > input[name=\"id\"]").send_keys("79755")
        driver.find_element_by_css_selector("input.query_btn").click()

        cc_name = driver.find_element_by_class_name("cc_name").text
        self.assertEqual(cc_name, "R&D Tools")

        driver.find_element_by_link_text("Sign off").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":

    # Add tests to suite
    suite = unittest.TestSuite()
    suite.addTest(PrmTest("test_prm"))

    # define test report
    filename = "/home/selenium/sauce-python-demo/prm_demo/result.html"
    fp = file(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="The PRM test report",
                                           description="Test case result:")
    runner.run(suite)

    fp.close()
