import time
import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLUtils
import os

class Test_Login_DDT():

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    # path = os.path.abspath(os.curdir)+"\\testdata\\test_open_cart.xlsx"
    path = r"D:\pytest-framework-by-sdet\pytest-by-sdet\testData\test_open_cart.xlsx"


    def test_login_ddt(self,setup):
        self.logger.info("*** Starting test_003_login_ddt******")
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2, self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path, "Sheet1",r,1)
            self.password = XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)
            print("Sheet----->",self.exp)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(6)

            self.targetpage = self.lp.isMyAccountPageExists()

            if self.exp =='Valid':
                if self.targetpage == True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')    

            elif self.exp == 'Invalid':
                if self.targetpage ==True:
                    lst_status.append('Fail')    
                    self.ma.clickLogout()

                else: 
                    lst_status.append('Pass')

        self.driver.close()

        if "Fail" not in lst_status:
            assert True

        else:
            assert False

        self.logger.info("**** End of test_003_login_datadriven *****")                            

