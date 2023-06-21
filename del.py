import base64
from selenium import webdriver

driver = webdriver.Chrome()
driver.set_script_timeout(10)

driver.get("https://www.allstatesusadirectory.com/submit.php")

driver.switch_to.frame("Main")

# find the captcha element
ele_captcha = driver.find_element("xpath", "//*[@id=main]/form/table/tbody/tr[12]/td[2]/img")

# get the captcha as a base64 string
img_captcha_base64 = driver.execute_async_script("""
    var ele = arguments[0], callback = arguments[1];
    ele.addEventListener('load', function fn(){
      ele.removeEventListener('load', fn, false);
      var cnv = document.createElement('canvas');
      cnv.width = this.width; cnv.height = this.height;
      cnv.getContext('2d').drawImage(this, 0, 0);
      callback(cnv.toDataURL('image/jpeg').substring(22));
    }, false);
    ele.dispatchEvent(new Event('load'));
    """, ele_captcha)

# save the captcha to a file
with open(r"captcha.jpg", 'wb') as f:
    f.write(base64.b64decode(img_captcha_base64))