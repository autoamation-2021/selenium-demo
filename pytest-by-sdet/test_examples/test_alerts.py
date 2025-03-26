from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytesseract
from PIL import Image
import base64
import io
import requests

driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
# time.sleep(3)

# alert_window = driver.switch_to.alert
# print(alert_window.text)

# alert_window.send_keys("Python Selenium")
# time.sleep(4)
# alert_window.accept()
# time.sleep(4)

# result_text = driver.find_element(By.ID,"result").text

# if result_text.__contains__("Python Selenium"):
#     print("Result is true: ",result_text)

# else:
#     print("Result is false")

# driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
# driver.find_element(By.ID,"login1").send_keys("sreekartest")
# driver.find_element(By.ID,"password").send_keys("Admin123$")
# driver.find_element(By.XPATH,"//input[@type='submit' and @value= 'Sign in'] ").click()

# time.sleep(5)

# captcha_image = driver.find_element(By.ID,"captchaimg")
# captcha_image_src = captcha_image.get_attribute("src")
# print("Captcha image source: ",captcha_image_src )

# if captcha_image_src.startswith('data:image'):
#     image_data = captcha_image_src.split('base64')[1]

#     image_bytes = base64.b64decode(image_data)

#     image = Image.open(io.BytesIO(image_bytes))

# else:
#     image_url = captcha_image_src
#     image = Image.open(requests.get(image_url,stream = True).raw)


# image.save("captcha.png")
# image.show()

# captcha_image_result = Image.open(captcha.png)
# captcha_text = pytesseract.image_to_string(captcha_image)

# # Print the extracted text
# print("Extracted CAPTCHA Text:", captcha_text)

#=============================================================================
# import requests
# from PIL import Image, ImageEnhance, ImageFilter
# from io import BytesIO
# import pytesseract

# # Specify the path to the Tesseract executable
# # Update this path based on your installation
# pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'

# image_url = 'https://mail.rediff.com/action/showcaptcha'  # Your image URL here

# response = requests.get(image_url, stream=True)

# # Ensure the content is an image
# if response.status_code == 200 and 'image' in response.headers.get('Content-Type', ''):
#     try:
#         # Open the image directly from the response stream
#         image = Image.open(BytesIO(response.content))

#         # Convert image to grayscale
#         image = image.convert('L')

#         # Enhance contrast
#         enhancer = ImageEnhance.Contrast(image)
#         image = enhancer.enhance(2)

#         # Apply a binary threshold to the image
#         threshold = 140
#         image = image.point(lambda p: p > threshold and 255)

#         # Remove noise by applying a median filter
#         image = image.filter(ImageFilter.MedianFilter())

#         # Define Tesseract configuration
#         custom_config = r'--oem 3 --psm 8'

#         # Use pytesseract to extract text from the image
#         captcha_text = pytesseract.image_to_string(image, config=custom_config)

#         print(f'Captcha Text: {captcha_text.strip()}')

#     except Exception as e:
#         print(f'Error processing image: {e}')
# else:
#     print('The URL does not return a valid image or failed to fetch the image.')

##########################################################################################

#alert pop-up
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(5)
alert_window = driver.switch_to.alert
alert_window.dismiss()
