import time

import pytest
from PageObjects.LoginPage import Loginpage
from Utilities.readproperties import Readconfig
from Utilities.Customlogger import Logging

class Test_001_login:

    url=Readconfig.geturl()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()
    logger=Logging.log()

    def loginfo(self,info):
        return self.logger.info("+"*8+info+"+"*8)

    def logerror(self,error):
        return self.logger.error("+"*8+error+"+"*8)

    def test_home_page(self,setup):
        self.loginfo("Test001_login ")
        self.loginfo("verifying Home Page title")
        self.driver=setup
        self.driver.get(self.url)
        exp_title="OrangeHRM"
        act_title=self.driver.title
        self.loginfo("comparing actual and expected title")
        if exp_title == act_title:
            assert True
            self.loginfo("HomePage Test Passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//homepage.png")
            self.logerror("HomePage Test Failed")
            assert False

    def test_login(self,setup):
        self.loginfo("verifying the login test")
        self.driver=setup
        self.lp=Loginpage(self.driver)
        self.driver.get(self.url)
        time.sleep(5)

        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.clicklogin()
        self.loginfo("clicked login button")
        exp_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        if self.driver.current_url==exp_url:
            self.loginfo("Login test passed")
            assert True
            self.driver.close()
        else:
            self.logerror("Login test failed")
            self.driver.save_screenshot(".//Screenshots//loginpage.png")
