import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login:

    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_Page_Title_001(self, setup):
        self.driver = setup
        self.log.info("test_Page_Title_001 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)

        # driver = webdriver.Firefox()
        # driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")

        if self.driver.title == "OrangeHRM":
            assert True
            self.log.info("test_Page_Title_001 is Passed")
            self.log.info("Page Title is-->" + self.driver.title)
        else:
            self.log.info("test_Page_Title_001 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_Page_Title_001 is completed")
        ###############################################
        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("critical")
        #############################################

    def test_login_002(self, setup):
        self.driver = setup
        self.log.info("test_login_002 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)

        # driver = webdriver.Firefox()
        # driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")

        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering username-->" + self.username)

        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")

        self.lp.Enter_Password(self.password)
        self.log.info("Entering password-->" + self.password)

        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")

        self.lp.Click_login()
        self.log.info("Click on login button")

        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # try:
        #     self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        #     print("test_login_001 is Passed")
        #     self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        #     self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #     login = True
        #     # assert True
        #     print(login)
        # except Ec:
        #     print("test_login_001 is Failed")
        #     print("test_login_001 is completed")
        #     login = False
        #     print(login)
        #     # assert False
        # if login == True:
        #     assert True
        # else:
        #     assert False
        # print(self.lp.Login_Status())


        if self.lp.Login_Status() == True:

            self.lp.Click_Menu()
            self.log.info("Click on Menu button")
            self.lp.Click_logout()
            self.log.info("Click on logout button")
            self.log.info("test_login_002 is Passed")
            assert True
        else:
            self.log.info("test_login_002 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_login_002 is Completed")
