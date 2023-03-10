# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# web = webdriver.Chrome()
# from selenium.webdriver.support.ui import Select
# web.get('https://gainweb.org/submit.php')
# web.maximize_window()

# time.sleep

# Title = " Why Is Web App Consulting Service Important For Your Business?"
# URL = "https://www.desss.com/blog/Why-Is-Web-App-Consulting-Service-Important-For-Your-Business"
# Description = "Optimizing your website creates a strong web presence for your brand. Read a few other reasons too, that state why web app consulting Houston is important for your business."
# Name = "michaeljohnde"
# Email = "desss1seo@gmail.com"
# key = "Web App Consulting"
# dess = "Optimizing your website creates a strong web presence for your brand. Read a few other reasons too, that state why web app consulting Houston is important for your business."
# regular_free = web.find_elements(By.XPATH, '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr[3]/td[1]/input')
# regular_free[0].click()

# tit = web.find_elements(By.XPATH, '//*[@id="TITLE"]')
# tit[0].send_keys(Title)
# print('ok')


# link = web.find_elements(By.XPATH, '//*[@id="URL"]')
# link[0].send_keys(URL)
# time.sleep(4)

# element=web.find_elements(By.NAME, ('CATEGORY_ID'))
# #print('ok')
# drp=Select(element[0])
# #print('ok')

# drp.select_by_visible_text('|   |   |___Internet and Web')

# des = web.find_elements(By.XPATH, '//*[@id="DESCRIPTION"]')
# des[0].send_keys(Description)
# time.sleep(4)

# yourname = web.find_elements(By.XPATH, '//*[@id="OWNER_NAME"]')
# yourname[0].send_keys(Name)
# time.sleep(3)

# mail = web.find_elements(By.XPATH, '//*[@id="OWNER_EMAIL"]')
# mail[0].send_keys(Email)
# time.sleep(3)

# meta_keywords = web.find_elements(By.NAME, 'META_KEYWORDS')
# meta_keywords[0].send_keys(key)
# time.sleep(2)

# meta_des = web.find_elements(By.NAME, 'META_DESCRIPTION')
# meta_des[0].send_keys(dess)
# time.sleep(3)
# agree = web.find_elements(By.NAME, 'AGREERULES')
# agree[0].click()
# time.sleep(10)
# print('i agree')
# submit = web.find_elements(By.XPATH, '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[13]/td/input')
# submit[0].click()
# time.sleep(5)
# web.quit()




































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
        driver.get('https://gainweb.org/submit.php')
        driver.maximize_window()
        time.sleep(5)

        freelink = driver.find_element("xpath", '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr[3]/td[1]/input')
        freelink.click()
        time.sleep(5)

        username_field = driver.find_element("xpath", '//*[@id="OWNER_NAME"]')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '//*[@id="OWNER_EMAIL"]')
        Email_field.send_keys(line[1])
        time.sleep(3)

        URL_field = driver.find_element("xpath", '//*[@id="URL"]')
        URL_field.send_keys(line[2])
        time.sleep(3)

        Title_field = driver.find_element("xpath", '//*[@id="TITLE"]')
        Title_field.send_keys(line[3])
        time.sleep(3)

        Description_field = driver.find_element("xpath", '//*[@id="DESCRIPTION"]')
        Description_field.send_keys(line[4])
        time.sleep(3)

        # Category_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select')
        # Category_field.send_keys(line[7])
        

        element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("|   |   |___Internet and Web")
        time.sleep(4)

        agree = driver.find_elements(By.NAME, 'AGREERULES')
        agree[0].click()
        time.sleep(10)

        submit = driver.find_elements(By.XPATH, '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[13]/td/input')
        submit[0].click()



#-------------------------------------------------------------------------------



