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
        driver.get('https://www.usalistingdirectory.com/submit.php')
        driver.maximize_window()
        time.sleep(5)

        regular_links = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/input')
        regular_links.click()
        time.sleep(5)

        Title_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/input')
        Title_field.send_keys(line[3])
        time.sleep(3)

        URL_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input')
        URL_field.send_keys(line[2])
        time.sleep(3)

        Description_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/textarea')
        Description_field.send_keys(line[4])
        time.sleep(3)

        username_field = driver.find_element("xpath",'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[8]/td[2]/input')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[9]/td[2]/input')
        Email_field.send_keys(line[1])
        time.sleep(3)

  

        # Category_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select')
        # Category_field.send_keys(line[7])
        

        element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("|   |   |___Internet and Web Skills")
        time.sleep(4)

        agree = driver.find_elements(By.NAME, 'AGREERULES')
        agree[0].click()
        time.sleep(10)

        submit = driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[13]/td/input')
        submit[0].click()



#-------------------------------------------------------------------------------



