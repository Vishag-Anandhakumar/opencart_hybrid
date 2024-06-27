import os
import time

import pytest

from page_objects.homePage import HomePage
from page_objects.loginPage import LoginPage
from page_objects.myAccountPage import MyAccountPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from utilities import XLUtils

class TestLoginNegative():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGeneration.logGen()

    #Specify the Excel sheet path
    path = os.path.abspath(os.curdir)+"\\test_data\\resources.xlsx"

    @pytest.mark.regression
    def test_negative_login_case(self, driverSetup):
        self.logger.info('************** Test started **************')
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lstStatus = []

        self.driver = driverSetup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.myAccountPage = MyAccountPage(self.driver)

        for row in range(2, self.rows+1):
            self.homePage.clickMyAccount()

            self.email = XLUtils.readData(self.path, 'Sheet1', row, 1)
            self.pwd = XLUtils.readData(self.path, 'Sheet1', row, 2)
            self.expectedResult = XLUtils.readData(self.path, 'Sheet1', row, 3)

            self.loginPage.enter_email_id(self.email)
            self.loginPage.enter_pwd(self.pwd)
            self.loginPage.click_login()
            time.sleep(3)

            self.targetPage = self.loginPage.is_my_account_displayed()
            if self.expectedResult == 'Valid':
                if self.targetPage == True:
                    lstStatus.append('Pass')
                    self.myAccountPage.log_out()
                else:
                    lstStatus.append('Fail')
            elif self.expectedResult == 'Invalid':
                if self.targetPage == True:
                    lstStatus.append('Fail')
                    self.myAccountPage.log_out()
                else:
                    lstStatus.append('Pass')
        self.driver.close()
        print(lstStatus)
        #Final validation
        if 'Fail' not in lstStatus:
            assert True
        else:
            assert False