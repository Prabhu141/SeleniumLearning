from PIL import Image
from selenium import webdriver
from PIL import Image, ImageFilter
import time  
import base64
import pytesseract
from PIL import Image
# import pytesseract 


driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\chromedriver\chromedriver.exe")
driver.get("http://www.yellowlinker.com/submit.php")

# def get_captcha(driver, element, path):
#     # now that we have the preliminary stuff out of the way time to get that image :D
#     location = element.location
#     size = element.size
#     # saves screenshot of entire page
#     driver.save_screenshot(path)

#     # uses PIL library to open image in memory
#     image = Image.open(path)

#     left = location['x']
#     top = location['y'] + 140
#     right = location['x'] + size['width']
#     bottom = location['y'] + size['height'] + 140

#     image = image.crop((left, top, right, bottom))  # defines crop points
#     image.save(path, 'png')  # saves new cropped image
    

#     # captcha = pytesseract.image_to_string(image) 
#     # captcha = captcha.replace(" ", "").strip()
#     # print(captcha)
#     return path




# download image/captcha
ele_captcha  = driver.find_element("xpath","/html/body/div[1]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[23]/td[2]/img")
# get_captcha(driver, img, "captcha.png")

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

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe' 
# Open the .jpg file
image = Image.open("captcha.jpg")

# Perform OCR using Tesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
time.sleep(10)
driver.close()