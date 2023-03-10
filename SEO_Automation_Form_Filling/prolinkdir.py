from selenium import webdriver
import time
import csv
import requests
from selenium.webdriver.common.by import By
web = webdriver.Chrome()
from selenium.webdriver.support.ui import Select

time.sleep

#this link not working the automation

Username = 0
Email = 1
with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)


    for line in csv_reader:
        driver = webdriver.Chrome()
        driver.get('https://www.prolinkdirectory.com/submit.php')
        driver.maximize_window()
        time.sleep(5)

        regular_free = web.find_elements(By.XPATH, '//*[@id="l3"]')
        regular_free[0].click()

        tit = web.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input')
        tit[0].send_keys(line[3])
        print('ok')


        link = web.find_elements(By.XPATH, '//*[@id="URL"]')
        link[0].send_keys(line[2])
        time.sleep(5)

        #category not filled
        element=web.find_elements(By.NAME, ('CATEGORY_ID'))
    
        drp=Select(element[0])
      

        drp.select_by_visible_text('|   |   |___Internet and Web')

        des = web.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/textarea')
        des[0].send_keys(line[4])
        time.sleep(4)

        yourname = web.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[14]/td[2]/input')
        yourname[0].send_keys(line[0])
        time.sleep(3)

        mail = web.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[15]/td[2]/input')
        mail[0].send_keys(line[1])
        time.sleep(3)

        # meta_keywords = web.find_elements(By.NAME, 'META_KEYWORDS')
        # meta_keywords[0].send_keys(line[5])
        # time.sleep(2)

        # meta_des = web.find_elements(By.NAME, 'META_DESCRIPTION')
        # meta_des[0].send_keys(line[0])
        # time.sleep(3)
        # agree = web.find_elements(By.XPATH, '//*[@id="AGREERULES"]')
        # agree[0].click()
        # time.sleep(7)
        # print('i agree')
        scontinue = web.find_elements(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[19]/td/input')
        scontinue[0].click()
        time.sleep(5)
        web.quit()
