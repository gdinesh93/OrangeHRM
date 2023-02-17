from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        print("launching chrome")
        from selenium.webdriver.chrome.service import Service

        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser=="firefox":
        print("launching firefox")
        from selenium.webdriver.firefox.service import Service

        driver = webdriver.Firefox(executable_path=Service(GeckoDriverManager().install()))
    else:
        print("launching edge")
        from selenium.webdriver.edge.service import Service

        driver = webdriver.Edge(service=Service("C:\\Users\\HP\\Downloads\\msedgedriver.exe"))

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['project Name'] = "OrangeHRM"
    config._metadata['Module Name'] = "HR"
    config._metadata['Tester'] = "Dinesh"
