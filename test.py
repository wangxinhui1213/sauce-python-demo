#!/usr/bin/python
# _*_ coding: utf-8 _*_

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()  # Get local session of firefox
browser.get("https://www.baidu.com")  # Load page

browser.find_element_by_id("kw").send_keys("webdriver")
browser.find_element_by_id("su").click()

browser.implicitly_wait(30)
print ("The result is right")
browser.quit()
