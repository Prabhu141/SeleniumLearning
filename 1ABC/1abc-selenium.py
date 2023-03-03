from selenium import webdriver
import time
from selenium.webdriver.common.by import By
web = webdriver.Chrome()
from selenium.webdriver.support.ui import Select
web.get('http://www.1abc.org/submit.php')
web.maximize_window()

time.sleep

Title = " Why Is Web App Consulting Service Important For Your Business?"
URL = "https://www.desss.com/blog/Why-Is-Web-App-Consulting-Service-Important-For-Your-Business"
Description = "Optimizing your website creates a strong web presence for your brand. Read a few other reasons too, that state why web app consulting Houston is important for your business."
Name = "michaeljohnde"
Email = "mailto:desss1seo@gmail.com"

free = web.find_elements(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/form/table[1]/tbody/tr/td/table/tbody/tr[4]/td[1]/input')
free[0].click()

tit = web.find_elements(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/input')
tit[0].send_keys(Title)
print('ok')
#time.sleep(5)

link = web.find_elements(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/input')
link[0].send_keys(URL)

des = web.find_elements(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/textarea')
des[0].send_keys(Description)


yourname = web.find_elements(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[4]/td[2]/input')
yourname[0].send_keys(Name)


mail = web.find_elements(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]/input')
mail[0].send_keys(Email)

# category = web.find_elements(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select')
# #category[0].send_keys(Email)

# x = web.find_elements(By.NAME, ('CATEGORY_ID'))
# drop=Select(category)
element=web.find_elements(By.NAME, ('CATEGORY_ID'))
print('ok')
drp=Select(element[0])
print('ok')

drp.select_by_visible_text('|   |___Web Development')
#drp.select_by_value("206")
# time.sleep(15)


# select by visible text
# drop.select_by_visible_text("|   |___Web Development")

submit = web.find_elements(By.XPATH, '/html/body/div/div/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[8]/td[2]/input')
submit[0].click()
web.quit()





















