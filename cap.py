from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# url1 = 'https://www.google.com/recaptcha/api2/demo'

# driver.get(url1)

# #addbutton = driver.find_element(By.CSS_SELECTOR, ".addToCartButton")
# addbutton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".addToCartButton")))
        
        
# # add to cart
# addbutton.click()

# print("done adding to cart.. going to signin to checkout now")
        
# time.sleep(7)

        
# go to cart
# driver.get("https://www.google.com/recaptcha/api2/demo")

# time.sleep(7)

#go to checkout
driver.get("https://www.google.com/recaptcha/api2/demo")

# print("arrived at signin")
        
# #user = driver.find_element_by_id("username")
# user = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
# user.send_keys("username@gmail.com")
# time.sleep(0.1)

    
# time.sleep(1)
        
# password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "password")))
    
 

# password.send_keys("password")
# time.sleep(0.15)

# print("entered username and password")
    
# time.sleep(1.25)



# signInBtn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/form/div/button")))
# time.sleep(3)
# signInBtn.click()

# print("signed in.")

try:    
   # driver.switch_to.frame('c-xsgh29r4he3')
   frame = driver.find_element("xpath","//*[@id=recaptcha-demo]/div/div/iframe")
   print("made it!")
   driver.switch_to.frame(frame)
   print("we made it!")

   time.sleep(5)
   

   #audiobutton = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button")
   audiobutton = driver.find_element("id","recaptcha-audio-button")
   audiobutton.click()   


   
   print("complete")
finally:
    test = ""
