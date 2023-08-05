import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import loginpage
from pageObjects.AddEmp_Page import AddEmployee
from utilities.Logger import LogGenerator

from utilities.readproperties import Readconfig


class Test_Add_Emp:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_addEmp_003(self, setup):
        self.driver = setup
        self.log.info("test_addEmp_003 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)

        self.lp = loginpage(self.driver)
        self.ae = AddEmployee(self.driver)

        self.lp.Enter_UserName(self.Username)
        self.log.info("Entering username-->" + self.Username)
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering username-->" + self.Password)

        self.driver.implicitly_wait(5)

        self.lp.Click_login()
        self.log.info("Click on login button")
        self.driver.implicitly_wait(5)

        self.ae.Click_PIM()
        self.log.info("Click on PIM button")

        self.ae.Click_Add()
        self.log.info("Click on Add button")

        self.ae.Enter_FirstName("Credence")
        self.log.info("First Name")

        self.ae.Enter_MiddleName("It")
        self.log.info("Middle Name")

        self.ae.Enter_LastName("Pune")
        self.log.info("Last Name")

        time.sleep(3)

        self.ae.Click_Save()
        self.log.info("Click on Save button")

        time.sleep(3)

        if self.ae.AddEmp_status() == True:
            self.driver.save_screenshot(
                "C:\\Users\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\OrangeHrm\\Screenshots\\test_addemp_pass.png")

            self.lp.Click_Menu()
            self.log.info("Click on Menu")

            self.lp.Click_logout()
            self.log.info("Click on logout button")

            self.driver.close()
            assert True
            self.log.info("test_addEmp_003 is passed")
        else:
            self.driver.save_screenshot(
                "C:\\Users\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\OrangeHrm\\Screenshots\\test_addemp_fail.png")

            self.log.info("test_addEmp_003 is failed")
            assert False
        self.log.info("test_addEmp_003 is completed")
