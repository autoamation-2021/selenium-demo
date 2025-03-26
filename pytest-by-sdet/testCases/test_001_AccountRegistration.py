from pageObjects.HomePage import HomePage    
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import utilities.randomString
import time
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("***test_001_AccountRegistration started***")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.logger.info("Launching application")

        self.driver.maximize_window()
        time.sleep(3)
        self.hp = HomePage(self.driver)
        self.logger.info("clicking on My Account->register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.info("Providing customer details for registration")
        time.sleep(3)
        self.regpage.setFirstName("Sreekar")
        self.regpage.setLastName("SV")
        # self.regpage.setEmail("abc@gmail.com")
        self.email = utilities.randomString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        # self.setTelephone("9393939393")
        self.regpage.setPassword("Admin123$")
        time.sleep(6)
    
        self.regpage.setPrivacyPolicy()
        time.sleep(4)
        self.regpage.setClickContinue()
        time.sleep(4)

        self.confmsg = self.regpage.getConfirmationMessage()

        if self.confmsg =="Your Account Has Been Created!":
            self.logger.info("Account Registration is passed")
            assert True
            self.driver.close()

        else:
            absolute_path = os.getcwd()
            print("===============================")
            print(absolute_path)
            print("===============================")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots"+"\\test_account_reg.png")
            self.logger.error("Account Registration is failed")
            self.driver.close()
            assert False   

        self.logger.info("***test_001_AccountRegistration finished***")     