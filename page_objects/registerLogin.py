from selenium.webdriver.common.by import By

class RegisterLogin():
    #Locators
    txt_email_id = 'reg_email'
    txt_password_id = 'reg_password'
    btn_register_xpath = '//*[@id="customer_login"]/div[2]/form/p[3]/input[3]'
    txt_msg_conf_xpath = '//*[@id="page-36"]/div/div[1]/div/p[1]'

    #Constructor
    def __init__(self, driver):
        self.driver = driver

    #Action methods
    def enterEmailId(self, emailId):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(emailId)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()

    def getSuccessMessage(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_msg_conf_xpath).text
        except:
            None

