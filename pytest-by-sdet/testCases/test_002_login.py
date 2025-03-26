import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
import time


class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("************ Starting test_002_login ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        print("user:",self.user)
        print("password:",self.password)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(3)

        self.targetpage = self.lp.isMyAccountPageExists()
        if self.targetpage == True:
            assert True

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login.png")  
            assert False

        self.driver.close()
        self.logger.info("****End of test_002_login*****")      
