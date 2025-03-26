from selenium import webdriver
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
import time

test_driver = webdriver.Chrome()
solver = RecaptchaSolver(driver=test_driver)
test_driver.get('https://assessment.shoplocal.digital/')
time.sleep(4)

recaptcha_element = test_driver.find_element(By.XPATH, '//*[@class="g-recaptcha"]')
solver.click_recaptcha_v2(element=recaptcha_element)

# site_key = driver.find_element("xpath", '//*[@class="g-recaptcha"]').get_attribute("data-sitekey")    