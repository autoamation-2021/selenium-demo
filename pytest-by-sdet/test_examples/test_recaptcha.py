from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

## Instantiate the WebDriver
driver = webdriver.Chrome()

## Load the target page
captcha_page_url = "https://assessment.shoplocalmms.com/"
driver.get(captcha_page_url)

## Solve the Captcha
print("Solving Captcha")
solver = TwoCaptcha("220cb984107c9395f62265bdcb518ee5")
response = solver.recaptcha(sitekey='6LeHWb8qAAAAAMLfHqyPTZs0nXAwd8gd3-uRFJmu', url=captcha_page_url)
code = response['code']
print(f"Successfully solved the Captcha. The solve code is {code}")