# https://github.com/2captcha/2captcha-python

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', '40354e663857b27f4419efc0294aca80')

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6LdkBmoUAAAAANqhkJtB29hcBLLajcO0uWlli78-',
        url='https://www.pr8directory.com/submit-url')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))

    