from selenium.webdriver.common.by import By

class AccountRegistrationPage:
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    # txt_telephone_name = "telephone"
    txt_password_name = "password"
    chk_policy_name_xpath = "//input[@name='agree']"
    btn_cont_xpath = "//button[text()='Continue']"
    txt_msg_conf_xpath = "//div[@id='content']/h1[text()='Your Account Has Been Created!']"


    def __init__(self,driver):
        self.driver = driver

    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)
    

    # def setTelephone(self,pwd):
    #     self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)   

    def setPrivacyPolicy(self):
        self.element = self.driver.find_element(By.XPATH,self.chk_policy_name_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.element)
        self.driver.execute_script("arguments[0].click();", self.element)
        # self.element.click()
        

    def setClickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_cont_xpath).click()  


    def getConfirmationMessage(self):
        # print("actual text====",self.driver.find_element(By.XPATH,self.txt_msg_conf_xpath).text)
        try:
            return self.driver.find_element(By.XPATH,self.txt_msg_conf_xpath).text

        except:
            None     



