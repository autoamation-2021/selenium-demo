from selenium.webdriver.common.by import By

class LoginPage():
    txt_email_id = "input-email"
    txt_password_id = "input-password"
    btn_login_xpath = "//button[text()='Login']"
    msg_account_xpath = "//h1[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def clickLogin(self):
        self.login_btn = self.driver.find_element(By.XPATH,self.btn_login_xpath)
        self.driver.execute_script("arguments[0].click();", self.login_btn)


    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_account_xpath).is_displayed()

        except:
            return False                    