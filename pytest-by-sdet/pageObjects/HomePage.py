from selenium.webdriver.common.by import By

class HomePage:
    my_account_by_link_text = "My Account"
    register_by_link_text = "Register"
    login_button_by_link_text = "Login"

    def __init__(self,driver):
        self.driver = driver


    def clickMyAccount(self):
        self.driver.find_element(By.LINK_TEXT,self.my_account_by_link_text).click()


    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.register_by_link_text).click()


    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.login_button_by_link_text).click() 
