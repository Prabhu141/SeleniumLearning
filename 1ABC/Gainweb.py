from selenium import webdriver
import time
from selenium.webdriver.common.by import By
web = webdriver.Chrome()
from selenium.webdriver.support.ui import Select
web.get('https://gainweb.org/submit.php')
web.maximize_window()

time.sleep

Title = " Why Is Web App Consulting Service Important For Your Business?"
URL = "https://www.desss.com/blog/Why-Is-Web-App-Consulting-Service-Important-For-Your-Business"
Description = "Optimizing your website creates a strong web presence for your brand. Read a few other reasons too, that state why web app consulting Houston is important for your business."
Name = "michaeljohnde"
Email = "desss1seo@gmail.com"
key = "Web App Consulting"
dess = "Optimizing your website creates a strong web presence for your brand. Read a few other reasons too, that state why web app consulting Houston is important for your business."
regular_free = web.find_elements(By.XPATH, '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr[3]/td[1]/input')
regular_free[0].click()

tit = web.find_elements(By.XPATH, '//*[@id="TITLE"]')
tit[0].send_keys(Title)
print('ok')


link = web.find_elements(By.XPATH, '//*[@id="URL"]')
link[0].send_keys(URL)
time.sleep(4)

element=web.find_elements(By.NAME, ('CATEGORY_ID'))
#print('ok')
drp=Select(element[0])
#print('ok')

drp.select_by_visible_text('|   |   |___Internet and Web')

des = web.find_elements(By.XPATH, '//*[@id="DESCRIPTION"]')
des[0].send_keys(Description)
time.sleep(4)

yourname = web.find_elements(By.XPATH, '//*[@id="OWNER_NAME"]')
yourname[0].send_keys(Name)
time.sleep(3)

mail = web.find_elements(By.XPATH, '//*[@id="OWNER_EMAIL"]')
mail[0].send_keys(Email)
time.sleep(3)

meta_keywords = web.find_elements(By.NAME, 'META_KEYWORDS')
meta_keywords[0].send_keys(key)
time.sleep(2)

meta_des = web.find_elements(By.NAME, 'META_DESCRIPTION')
meta_des[0].send_keys(dess)
time.sleep(3)
agree = web.find_elements(By.XPATH, '//*[@id="AGREERULES"]')
agree[0].click()
time.sleep(7)
print('i agree')
scontinue = web.find_elements(By.XPATH, '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[13]/td/input')
scontinue[0].click()
time.sleep(5)
web.quit()




















