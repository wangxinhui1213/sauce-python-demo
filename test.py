#!/usr/bin/python
# _*_ coding: utf-8 _*_

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.so.com")
assert u"360搜索" in driver.title
print driver.title
driver.close()
