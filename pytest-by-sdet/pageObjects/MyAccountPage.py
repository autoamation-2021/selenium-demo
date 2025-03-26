from selenium.webdriver.common.by import By

class MyAccountPage():
    lnk_logout_xpath = "(//a[text()='Logout'])[1]"

    def __init__(self,driver):
        self.driver = driver


    def clickLogout(self):
        self.log_out_btn = self.driver.find_element(By.XPATH,self.lnk_logout_xpath)
        self.driver.execute_script("arguments[0].click();", self.log_out_btn)

