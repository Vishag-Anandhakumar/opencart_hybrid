from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    txt_email_id = 'username'
    txt_pwd_id = 'password'
    btn_login_name = 'login'
    msg_after_login_xpath = '//*[@id="page-36"]/div/div[1]/div/p[1]/strong'

    def __init__(self, driver):
        self.driver = driver

    def enter_email_id(self, emailId):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(emailId)

    def enter_pwd(self, pwd):
        self.driver.find_element(By.ID, self.txt_pwd_id).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(By.NAME, self.btn_login_name).click()

    def get_msg(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_after_login_xpath).text
        except:
            return False

    def is_my_account_displayed(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_after_login_xpath).is_displayed()
        except:
            return False
