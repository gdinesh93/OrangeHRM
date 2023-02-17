from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Loginpage:
    txt_username_xpath='//*[@name="username"]'
    txt_password_xpath='//*[@type="password"]'
    btn_login_xpath='//*[@type="submit"]'

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(By.XPATH,self.txt_username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
