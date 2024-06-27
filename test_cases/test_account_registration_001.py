import logging
import time
import os

import pytest

from page_objects.homePage import HomePage
from page_objects.registerLogin import RegisterLogin
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration


class TestAccountRegistration_001:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGeneration.logGen()

    @pytest.mark.sanity
    def test_account_registration(self, driverSetup):
        self.logger.info("********  test_account_registration started  *********")
        self.driver = driverSetup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.clickMyAccount()
        self.registrationPage = RegisterLogin(self.driver)
        self.email = randomString.random_string_generator()
        self.registrationPage.enterEmailId(self.email+'@abc.com')
        self.pwd = randomString.random_string_generator() + '1827'
        self.registrationPage.enterPassword(self.pwd)
        self.registrationPage.clickRegister()
        self.actualMessage = self.registrationPage.getSuccessMessage()
        print(self.actualMessage)
        # assert self.actualMessage == f'Hello {self.email} (not {self.email}? Sign out)'
        if self.actualMessage == f'Hello {self.email} (not {self.email}? Sign out)':
            self.driver.close()
            self.logger.setLevel(logging.INFO) #To add the logger statements
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\test_account_registration.png")
            self.logger.setLevel(logging.ERROR) #To add the error logs
            self.driver.close()
            assert False