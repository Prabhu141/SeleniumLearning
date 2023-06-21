

#-------------------------------------------------------------------------------
# Imports
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
#-------------------------------------------------------------------------------
# Setup
Username = 0
Email = 1
URL = 2

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('https://www.1websdirectory.com/submission/0/free-listing/')
        driver.maximize_window()
        #time.sleep(5)


        Title_field = driver.find_element("xpath", '//*[@id="main-body"]/div/div/div[4]/div[1]/div[2]/div[2]/form/div[2]/div[2]/input')
        Title_field.send_keys(line[3])
        time.sleep(3)
    
        Url_field = driver.find_element("xpath", '//*[@id="main-body"]/div/div/div[4]/div[1]/div[2]/div[2]/form/div[2]/div[1]/input')
        Url_field.send_keys(line[2])
        time.sleep(3)


        Description_field = driver.find_element("xpath", '//*[@id="main-body"]/div/div/div[4]/div[1]/div[2]/div[2]/form/div[3]/textarea')
        Description_field.send_keys(line[4])
        time.sleep(3)

        OWNER_NAME = driver.find_element("xpath", '//*[@id="main-body"]/div/div/div[4]/div[1]/div[2]/div[2]/form/div[4]/div[1]/input')
        OWNER_NAME.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '//*[@id="main-body"]/div/div/div[4]/div[1]/div[2]/div[2]/form/div[4]/div[2]/input')
        Email_field.send_keys(line[1])
        time.sleep(3)

        element=driver.find_elements(By.NAME, ('category'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("Internet")
        time.sleep(4)

        element=driver.find_elements(By.NAME, ('sub_category'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("Web Development")
        time.sleep(4)


        submit = driver.find_elements(By.XPATH, '//*[@id="main-body"]/div/div/div[4]/div[1]/div[2]/div[2]/form/div[6]/div[2]/input')
        submit[0].click()



#-------------------------------------------------------------------------------