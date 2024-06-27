from selenium import webdriver
from selenium.webdriver.common.by import By

class MyAccountPage():
    link_logout_linkText = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def log_out(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linkText).click()