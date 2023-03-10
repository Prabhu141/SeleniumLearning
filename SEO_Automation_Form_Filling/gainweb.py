from selenium import webdriver
import time
import csv
import requests
from selenium.webdriver.common.by import By
web = webdriver.Chrome()
from selenium.webdriver.support.ui import Select

time.sleep

Username = 0
Email = 1
with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)


    for line in csv_reader:
        driver = webdriver.Chrome()
        driver.get('https://gainweb.org/submit.php')
        driver.maximize_window()
        time.sleep(5)

        regular_free = web.find_elements(By.XPATH, '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr[3]/td[1]/input')
        regular_free[0].click()

        tit = web.find_elements(By.XPATH, '//*[@id="TITLE"]')
        tit[0].send_keys(line[3])
        print('ok')


        link = web.find_elements(By.XPATH, '//*[@id="URL"]')
        link[0].send_keys(line[2])
        time.sleep(5)

        element=web.find_elements(By.NAME, ('CATEGORY_ID'))
        #print('ok')
        drp=Select(element[0])
        #print('ok')

        drp.select_by_visible_text('|   |   |___Internet and Web')

        des = web.find_elements(By.XPATH, '//*[@id="DESCRIPTION"]')
        des[0].send_keys(line[4])
        time.sleep(4)

        yourname = web.find_elements(By.XPATH, '//*[@id="OWNER_NAME"]')
        yourname[0].send_keys(line[0])
        time.sleep(3)

        mail = web.find_elements(By.XPATH, '//*[@id="OWNER_EMAIL"]')
        mail[0].send_keys(line[1])
        time.sleep(3)

# meta_keywords = web.find_elements(By.NAME, 'META_KEYWORDS')
# meta_keywords[0].send_keys(line[5])
# time.sleep(2)

# meta_des = web.find_elements(By.NAME, 'META_DESCRIPTION')
# meta_des[0].send_keys(line[0])
# time.sleep(3)
        agree = web.find_elements(By.XPATH, '//*[@id="AGREERULES"]')
        agree[0].click()
        time.sleep(7)
        print('i agree')
        scontinue = web.find_elements(By.XPATH, '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[13]/td/input')
        scontinue[0].click()
        time.sleep(5)
        web.quit()




















