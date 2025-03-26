# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import requests
# import os
# import speech_recognition as sr
# from pydub import AudioSegment

# # Initialize WebDriver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# driver.maximize_window()
# driver.get("https://assessment.shoplocal.digital/assessment/form")
# time.sleep(5)

# # Step 1: Click on reCAPTCHA checkbox
# recaptcha_frame = driver.find_element(By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")
# driver.switch_to.frame(recaptcha_frame)
# driver.find_element(By.ID, "rc-anchor-container").click()
# time.sleep(5)
# driver.switch_to.default_content()

# try:
#     # Step 2: Check if image challenge appears
#     challenge_frame = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'recaptcha challenge')]"))
#     )
#     print("Image challenge detected, switching to audio challenge...")

#     # Switch to challenge iframe
#     driver.switch_to.frame(challenge_frame)

#     # Click on audio button
#     audio_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.ID, "recaptcha-audio-button"))
#     )
#     audio_button.click()
#     time.sleep(2)

#     # Step 3: Extract the Audio CAPTCHA URL
#     audio_src = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.ID, "audio-source"))
#     ).get_attribute("src")
#     print(f"Audio CAPTCHA URL: {audio_src}")

#     # Step 4: Download the audio file
#     response = requests.get(audio_src)
#     audio_file = "captcha_audio.mp3"

#     with open(audio_file, "wb") as file:
#         file.write(response.content)
#     print("Audio CAPTCHA downloaded successfully.")

#     # Convert MP3 to WAV
#     audio_wav = "captcha_audio.wav"
#     AudioSegment.from_mp3(audio_file).export(audio_wav, format="wav")

#     # Step 5: Transcribe the audio using Speech Recognition
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_wav) as source:
#         audio_data = recognizer.record(source)
#         captcha_text = recognizer.recognize_google(audio_data)
    
#     print(f"Recognized CAPTCHA Text: {captcha_text}")

#     # Step 6: Enter the CAPTCHA text in the input box
#     captcha_input = driver.find_element(By.ID, "audio-response")
#     captcha_input.send_keys(captcha_text)
#     captcha_input.send_keys(Keys.ENTER)
#     time.sleep(3)

#     # Check if reCAPTCHA is solved
#     if "verification succeeded" in driver.page_source.lower():
#         print("reCAPTCHA solved successfully!")
#     else:
#         print("Failed to solve reCAPTCHA.")

# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     driver.quit()
#     # Cleanup downloaded files
#     if os.path.exists(audio_file):
#         os.remove(audio_file)
#     if os.path.exists(audio_wav):
#         os.remove(audio_wav)

#===================================================================


import time
import requests
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pydub import AudioSegment
import os

# Set up Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://assessment.shoplocal.digital/assessment/form")

time.sleep(5)

# Switch to reCAPTCHA iframe
recaptcha_frame = driver.find_element(By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")
driver.switch_to.frame(recaptcha_frame)

# Click reCAPTCHA checkbox
driver.find_element(By.ID, "rc-anchor-container").click()
time.sleep(5)

# Switch back to main content
driver.switch_to.default_content()
time.sleep(3)

# Switch to second iframe (if image appears, switch to audio)
captcha_iframe = driver.find_element(By.XPATH, "//iframe[contains(@title, 'recaptcha challenge')]")
driver.switch_to.frame(captcha_iframe)

# Click on the audio challenge button
audio_button = driver.find_element(By.ID, "recaptcha-audio-button")
audio_button.click()
time.sleep(3)

# Find and download the audio file
audio_src = driver.find_element(By.XPATH, "//audio[@id='audio-source']").get_attribute("src")
audio_file_path = "captcha_audio.mp3"

# Download the audio file
response = requests.get(audio_src)
with open(audio_file_path, "wb") as f:
    f.write(response.content)

# Convert MP3 to WAV (for speech recognition)
audio = AudioSegment.from_mp3(audio_file_path)
audio.export("captcha_audio.wav", format="wav")

# Use Speech-to-Text API to convert the audio
recognizer = sr.Recognizer()
with sr.AudioFile("captcha_audio.wav") as source:
    audio_data = recognizer.record(source)
    captcha_text = recognizer.recognize_google(audio_data)

# Enter the text into the response box
response_box = driver.find_element(By.ID, "audio-response")
response_box.send_keys(captcha_text)
response_box.send_keys(Keys.ENTER)

# Wait and check if reCAPTCHA was solved
time.sleep(5)
driver.switch_to.default_content()

# If reCAPTCHA is solved, proceed
if "success" in driver.page_source:
    print("reCAPTCHA solved successfully!")
else:
    print("reCAPTCHA solving failed.")

# Clean up files
os.remove("captcha_audio.mp3")
os.remove("captcha_audio.wav")

# Close the browser
driver.quit()
