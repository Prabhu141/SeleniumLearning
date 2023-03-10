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
        driver.get('https://www.pr8directory.com/submit-url')
        driver.maximize_window()
        time.sleep(5)

        freelink = driver.find_element("xpath", '/html/body/div[2]/div/div[3]/div[2]/div[2]/form/input[1]')
        freelink.click()
        time.sleep(5)

        Title_field = driver.find_element("xpath", '/html/body/div[2]/div/div[3]/div[2]/div[2]/form/input[5]')
        Title_field.send_keys(line[3])
        time.sleep(3)

        URL_field = driver.find_element("xpath", '/html/body/div[2]/div/div[3]/div[2]/div[2]/form/input[6]')
        URL_field.send_keys(line[2])
        time.sleep(3)

        Description_field = driver.find_element("xpath", '/html/body/div[2]/div/div[3]/div[2]/div[2]/form/textarea[1]')
        Description_field.send_keys(line[4])
        time.sleep(3)

        username_field = driver.find_element("xpath", '/html/body/div[2]/div/div[3]/div[2]/div[2]/form/input[17]')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '/html/body/div[2]/div/div[3]/div[2]/div[2]/form/input[18]')
        Email_field.send_keys(line[1])
        time.sleep(3)

        element=driver.find_elements(By.NAME, ('category'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("-- --> Web Development")
        time.sleep(4)

        submit = driver.find_elements(By.XPATH, '//*[@id="submitbutton"]')
        submit[0].click()
