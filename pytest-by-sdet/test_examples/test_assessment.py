from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import requests

# Automatically downloads the right ChromeDriver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://assessment.shoplocal.digital/assessment/form")
time.sleep(5)
recaptcha_frame = driver.find_element(By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")
driver.switch_to.frame(recaptcha_frame)
driver.find_element(By.ID, "rc-anchor-container").click()
time.sleep(5)
driver.switch_to.default_content()
time.sleep(35)
response_token = driver.find_element("xpath", '//*[@class="g-recaptcha"]').get_attribute("data-sitekey")
response_token = driver.execute_script("return document.getElementsByClassName('g-recaptcha-response')[0].value")
print(response_token) 
print(type(response_token) )# Verify if it's correct



# secret_key = "6Lc4WL8qAAAAAN53Z4ekv4ZmK2unbES-VFtgVV1n"
# response_token = response_token  # Usually obtained from frontend
# time.sleep(5)
# verification_url = "https://www.google.com/recaptcha/api/siteverify"
# data = {
#     "secret": secret_key,
#     "response": response_token
# }

# response = requests.post(verification_url, data=data)
# print(response.json()) 


# driver.find_element(By.ID,"organizationName").send_keys("Meylah Corp")

# organization_type_drop_down = driver.find_element(By.ID,"organizationType")
# select_organization_type_drop_down = Select(organization_type_drop_down)
# select_organization_type_drop_down.select_by_visible_text("Media")
# time.sleep(4)

# driver.find_element(By.ID,"yourName").send_keys("Sreekar SV")
# driver.find_element(By.ID,"phoneNumber").send_keys("9999999999")

# your_role_drop_down = driver.find_element(By.ID,"yourRole")
# select_your_role_drop_down = Select(your_role_drop_down)
# select_your_role_drop_down.select_by_visible_text("Sales")
# time.sleep(4)


# driver.find_element(By.ID,"email_address").send_keys("sreekartest@iverbinden.com")

# country_drop_down = driver.find_element(By.ID,"country")
# select_country_drop_down = Select(country_drop_down)
# select_country_drop_down.select_by_visible_text("India")
# time.sleep(4)

# state_drop_down = driver.find_element(By.ID,"state")
# select_state_drop_down = Select(state_drop_down)
# select_state_drop_down.select_by_visible_text("Karnataka")
# time.sleep(4)

# driver.find_element(By.ID,"city").send_keys("Banglore")

# driver.find_element(By.ID, "postal_code").send_keys("98302")

# driver.find_element(By.ID, "website").send_keys("https://iverbinden.com/")
# time.sleep(3)

# driver.find_element(By.XPATH,"(//button//p[text()='Next'])[1]").click()
# time.sleep(5)

# #========================================================================

# members_drop_down = driver.find_element(By.ID,"question_7f41f2d3-c86c-469f-b700-a7fc72232a53")
# select_members_drop_down = Select(members_drop_down)
# select_members_drop_down.select_by_visible_text("01-50")
# time.sleep(4)

# business_members_drop_down = driver.find_element(By.ID,"question_e0718ba8-9c3f-47f7-ac1c-8546f47a17df")
# select_business_members_drop_down = Select(business_members_drop_down)
# select_business_members_drop_down.select_by_visible_text("01-50")
# time.sleep(4)



# audience_size_drop_down = driver.find_element(By.ID,"question_85c38351-f37a-4f3f-b777-154d4ce98000")
# select_audience_size_drop_down = Select(audience_size_drop_down)
# select_audience_size_drop_down.select_by_visible_text("25000-50000")
# time.sleep(4)

# staff_drop_down = driver.find_element(By.ID,"question_b9fb0d27-6141-41ab-995f-29b005b3b685")
# select_audience_size_drop_down = Select(audience_size_drop_down)
# select_audience_size_drop_down.select_by_visible_text("1")
# time.sleep(4)

# email_distribution_drop_down = driver.find_element(By.ID,"question_087c8f0a-6586-4796-bdc7-ca81cc65212e")
# select_email_distribution_drop_down = Select(email_distribution_drop_down)
# select_email_distribution_drop_down.select_by_visible_text("500-1000")
# time.sleep(4)

# social_media_followers_drop_down = driver.find_element(By.ID,"question_087c8f0a-6586-4796-bdc7-ca81cc65212e")
# select_social_media_followers_drop_down = Select(social_media_followers_drop_down)
# select_social_media_followers_drop_down.select_by_visible_text("500-1000")
# time.sleep(4)

# driver.find_element(By.XPATH,"(//button//p[text()='Next'])[2]").click()

# #==============================================

# grow_membership_drop_down = driver.find_element(By.ID,"question_bb08cb45-2408-44e2-aff2-3273cab4d67c")
# select_grow_membership_drop_down = Select(grow_membership_drop_down)
# select_grow_membership_drop_down.select_by_visible_text("Low")
# time.sleep(4)

# increaese_revenue_drop_down = driver.find_element(By.ID,"question_dc7b3b51-5e22-4977-be3c-e26e3b38061d")
# select_increaese_revenue_drop_down = Select(increaese_revenue_drop_down)
# select_increaese_revenue_drop_down.select_by_visible_text("Low")
# time.sleep(4)

# decrease_member_attrition_drop_down = driver.find_element(By.ID,"question_feb3546c-fb78-4b45-b815-16cc80d706c0")
# select_decrease_member_attrition_drop_down = Select(decrease_member_attrition_drop_down)
# select_decrease_member_attrition_drop_down.select_by_visible_text("Low")
# time.sleep(4)

# increase_events_drop_down = driver.find_element(By.ID,"question_19ff728a-fc70-4f46-a51c-5438ca94e970")
# select_increase_events_drop_down = Select(increase_events_drop_down)
# select_increase_events_drop_down.select_by_visible_text("Low")
# time.sleep(4)

# sponsorship_revenue_drop_down = driver.find_element(By.ID,"question_df3aa598-5a34-45d6-99f4-13ea95787e69")
# select_sponsorship_revenue_drop_down = Select(sponsorship_revenue_drop_down)
# select_sponsorship_revenue_drop_down.select_by_visible_text("Low")
# time.sleep(4)

# driver.find_element(By.XPATH,"(//button//p[text()='Submit'])").click()