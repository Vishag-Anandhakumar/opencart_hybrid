import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driverSetup(browser):
    if browser == 'edge':
        from selenium.webdriver.edge.service import Service
        from selenium.webdriver.edge.options import Options
        service = Service()
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(service=service, options=options)
    elif browser == 'firefox':
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.firefox.options import Options
        service = Service()
        options = Options()
        options.add_argument("--disable-notifications")
        # options.add_experimental_option("detach", True)
        driver = webdriver.Firefox(service=service, options=options)
    else:
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        import chromedriver_autoinstaller
        chromedriver_autoinstaller.install()
        service = Service()
        options = Options()
        options.add_argument("--disable-notifications")
        # options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service, options=options)
        # driver = webdriver.Chrome(ChromeDriverManager().install()) --------> To install the req drivers while running the code
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #--------------> this will return the browser value to setup method
    return request.config.getoption("--browser")

############ Generate HTML Report ################

#Hook to add env info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'AutomationPractice'
    config._metadata['Module Name'] = 'Account registration'
    config._metadata['Tester'] = 'Vishag A'

#Hook to delete/modify env info to HTML  Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)

#Specify report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"