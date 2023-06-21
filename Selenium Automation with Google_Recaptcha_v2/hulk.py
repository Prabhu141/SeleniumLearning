from selenium import webdriver
from capmonster_python import RecaptchaV2Task
from time import sleep


class RecaptchaV2Selenium:
    def __init__(self, _client_key, executable_path):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        self.captcha = RecaptchaV2Task(_client_key)
        self.browser = webdriver.Firefox(executable_path=executable_path)
        self.website_url = "https://www.google.com/recaptcha/api2/demo"

    def _get_site_key(self):
        self.browser.get("https://www.google.com/recaptcha/api2/demo")
        return self.browser.find_element_by_id("recaptcha-demo").get_attribute("data-sitekey")

    def _solve_recaptcha(self):
        self.captcha.set_user_agent(self.user_agent)
        task_id = self.captcha.create_task(website_url=self.website_url,
                                           website_key=self._get_site_key(),
                                           no_cache=True)
        return self.captcha.join_task_result(task_id=task_id, maximum_time=180).get("gRecaptchaResponse")

    def submit_form(self):
        self.browser.execute_script("document.getElementsByClassName('g-recaptcha-response')[0].innerHTML = "
                                    f"'{self._solve_recaptcha()}';")
        self.browser.find_element_by_id("recaptcha-demo-submit").click()
        sleep(10)
        self.browser.close()
        return self.browser.find_element_by_class_name("recaptcha-success")


if __name__ == "__main__":
    client_key = "client_key"
    executable_path = r"C:\Users\Admin\chromedriver"
    recaptcha_selenium = RecaptchaV2Selenium(client_key, executable_path)