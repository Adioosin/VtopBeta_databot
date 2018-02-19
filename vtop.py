# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:08:53 2018

@author: Aditya Sinha
"""

import os
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

executable_path = r"C:\Users\guest11\Documents\chromedriver\chromedriver.exe" #specify the path of chromedriver in your pc
#os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension(r'C:\Users\guest11\AppData\Local\Google\Chrome\User Data\Default\Extensions\hafeeaangmkbibcaahfjdmmmeappjbbp\2.2_0.crx') #make a packed copy of this extension i.e. .crx format and specify its path

driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
driver.get("https://vtopbeta.vit.ac.in/vtop/")
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)
email_field = driver.find_element_by_id("uname")
#email = input() 
email_field.send_keys("16BCE2306")
password_field = driver.find_element_by_id("passwd")
#password = input()
password_field.send_keys("Aditya@123")
password_field.send_keys(Keys.RETURN)
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)
print("hello")

#vtopbeta_data = driver.page_source
#soup_data = BeautifulSoup(vtopbeta_data,"html.parser")
#print(soup_data)

menu = driver.find_element_by_class_name("sidebar-toggle")
menu.click()
#academics = 
driver.find_element_by_xpath("//div[@id='dbMenu']//ul//span[contains(.,'ACADEMICS')]").click()