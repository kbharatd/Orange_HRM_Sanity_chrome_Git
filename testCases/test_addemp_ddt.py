import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import loginpage
from pageObjects.AddEmp_Page import AddEmployee
from utilities import XLutils

from utilities.Logger import LogGenerator

from utilities.readproperties import Readconfig




class Test_Add_Emp_DDT:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\OrangeHrm\\testCases\\TestData\\Employeelist.xlsx"

    def test_addEmp_ddt_005(self, setup):
        self.driver = setup
        self.log.info("test_addEmp_ddt_005 is started")
        self.log.info("Opening Browser")
        time.sleep(8)
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

        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Number of rows are-->", self.rows)

        self.ae.Click_PIM()
        self.log.info("Click on PIM button")

        self.ae.Click_Add()
        self.log.info("Click on Add button")

        status_list = []

        for r in range(2, self.rows + 1):
            self.FirstName = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.MiddleName = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.LastName = XLutils.readData(self.path, 'Sheet1', r, 4)

            self.ae.Enter_FirstName(self.FirstName)
            self.log.info("Entering First Name-->" + self.FirstName)

            self.ae.Enter_MiddleName(self.MiddleName)
            self.log.info("Entering Middle Name-->" + self.MiddleName)

            self.ae.Enter_LastName(self.LastName)
            self.log.info("Entering Last Name-->" + self.LastName)

            time.sleep(3)

            self.ae.Click_Save()
            self.log.info("Click on Save button")

            time.sleep(3)

            if self.ae.AddEmp_status() == True:
                self.ae.Click_AddEmployee()
                self.log.info("Click on Add_Emp")
                # self.driver.save_screenshot(
                #     "C:\\Users\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\OrangeHrm\\Screenshots\\test_addemp_pass.png")
                status_list.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 5, "pass")
                assert True

            else:
                # self.driver.save_screenshot(
                #     "C:\\Users\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\OrangeHrm\\Screenshots\\test_addemp_fail.png")
                status_list.append("Fail")
                XLutils.writeData(self.path, 'Sheet1', r, 5, "fail")

                assert False

        print(status_list)
        self.lp.Click_Menu()
        self.log.info("Click on Menu")

        self.lp.Click_logout()
        self.log.info("Click on logout button")

        if "Fail" not in status_list:
            assert True
            self.log.info("test_addEmp_ddt_005 is passed")

        else:
            self.log.info("test_addEmp_ddt_005 is failed")
            assert False

        self.log.info("test_addEmp_ddt_005 is completed")
