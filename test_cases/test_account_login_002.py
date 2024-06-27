import pytest

from page_objects.homePage import HomePage
from page_objects.loginPage import LoginPage
from page_objects.myAccountPage import MyAccountPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration

class TestLogin():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGeneration.logGen()
    user = ReadConfig.getUserEmail()
    pwd = ReadConfig.getPwd()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_account_login(self, driverSetup):
        self.logger.info('************* Test account login starts *************')
        self.driver = driverSetup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.homepage = HomePage(self.driver)
        self.homepage.clickMyAccount()

        self.loginpage = LoginPage(self.driver)
        self.loginpage.enter_email_id(self.user)
        self.loginpage.enter_pwd(self.pwd)
        self.loginpage.click_login()
        print(self.loginpage.get_msg())
        if self.loginpage.get_msg() in self.user:
            assert True
        else:
            assert False
        self.logout = MyAccountPage(self.driver)
        self.logout.log_out()
        self.driver.close()
