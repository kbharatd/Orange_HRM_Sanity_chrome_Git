import time

from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import loginpage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login_Params:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_login_params_004(self, setup, getDataforlogin):
        self.driver = setup
        self.log.info("test_login_002 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)

        # driver = webdriver.Firefox()
        # driver.implicitly_wait(10)
        # driver.get("https://opensource-demo.orangehrmlive.com/")

        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(getDataforlogin[0])
        self.log.info("Entering username-->" + getDataforlogin[0])

        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")

        self.lp.Enter_Password(getDataforlogin[1])
        self.log.info("Entering password-->" + getDataforlogin[1])

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
            if getDataforlogin[2] == "Pass":

                self.lp.Click_Menu()
                self.log.info("Click on Menu button")
                self.lp.Click_logout()
                self.log.info("Click on logout button")
                self.log.info("test_login_002 is Passed")
                assert True

            else:
                self.log.info("test_login_002 is Failed")
                assert False
        else:
            if getDataforlogin[2] == "Fail":
                assert True
            else:
                assert False

        self.driver.close()
        self.log.info("test_login_002 is Completed")
