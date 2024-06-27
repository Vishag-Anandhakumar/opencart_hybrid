from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage():
    #Locators
    link_myAccount_link_text = 'My Account'

    #Constructor
    def __init__(self, driver):
        self.driver = driver

    #Action methods
    def clickMyAccount(self):
        self.driver.find_element(By.LINK_TEXT, self.link_myAccount_link_text).click()