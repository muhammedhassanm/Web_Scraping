# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:14:15 2019

@author: Muhammed Hassan M
"""
import os
os.makedirs('./image/', exist_ok=True)
import selenium
print (selenium.__file__) 
from selenium.webdriver import chrome

driver = webdriver.Chrome()
driver.get("https://morvanzhou.github.io/")
driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
driver.find_element_by_link_text("About").click()
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"数据处理 ▾").click()
driver.find_element_by_link_text(u"网页爬虫").click()

html = driver.page_source       # get html
driver.get_screenshot_as_file("./img/sreenshot1.png")
driver.close()
print(html[:200])