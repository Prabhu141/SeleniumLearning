from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import SessionNotCreatedException
import time

options = webdriver.ChromeOptions()
download_dir = "C:/path/to/download/directory"

prefs = {"download.default_directory": download_dir}
options.add_experimental_option("prefs", prefs)
options.add_argument("--no-sandbox")
    
driver = webdriver.Chrome(r"C:\Users\Admin\chromedriver", chrome_options = options)
driver.get("https://www.google.com/recaptcha/api2/demo")
time.sleep(5) 
driver.maximize_window()
price = driver.find_element("xpath", "//div[@class='g-recaptcha']")
price_content = price.get_attribute('innerHTML')
start = str(price_content).find(";k=")+len(";k=")
end = str(price_content).find("&amp;co")
driver.implicitly_wait(20)
time.sleep(5)
driver.execute_script("document.getElementById('g-recaptcha-response').style.display = '';")
recaptcha_text_area = driver.find_element("id", "g-recaptcha-response")
time.sleep(5)    
recaptcha_text_area.clear()
recaptcha_text_area.send_keys(price_content[start:end])
    #.....................................................................................
time.sleep(5)   
button = driver.find_element("id", "recaptcha-demo-submit")