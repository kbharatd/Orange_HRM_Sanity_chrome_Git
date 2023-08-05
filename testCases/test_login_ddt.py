import time

import pytest

from pageObjects.LoginPage import loginpage
from utilities import XLutils
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login_DDT:
    Url = Readconfig.geturl()
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\OrangeHrm\\testCases\\TestData\\LoginData.xlsx"

    def test_login_ddt_006(self, setup):

        self.driver = setup
        self.log.info("test_login_ddt_006 is started")

        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)

        self.lp = loginpage(self.driver)

        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Number of rows are --->", self.rows)

        login_status = []
        for r in range(2, self.rows + 1):
            self.username = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 3)

            time.sleep(3)

            self.lp.Enter_UserName(self.username)
            self.log.info("Entering username-->" + self.username)

            self.lp.Enter_Password(self.password)
            self.log.info("Entering password-->" + self.password)

            time.sleep(3)

            self.lp.Click_login()
            self.log.info("Click on login button")

            time.sleep(3)

            if self.lp.Login_Status() == True:

                self.lp.Click_Menu()
                self.log.info("Click on Menu button")
                self.lp.Click_logout()
                self.log.info("Click on logout button")

                login_status.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Pass")
            else:

                login_status.append("Fail")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                time.sleep(5)

        print(login_status)
        if "Fail" not in login_status:
            self.log.info("test_login_ddt_006 is Passed")
            assert True
        else:
            self.log.info("test_login_ddt_006 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_login_ddt_006 is Completed")

# pytest -v -n=3 --html=Reports/report.html -m sanity -p no:warnings
