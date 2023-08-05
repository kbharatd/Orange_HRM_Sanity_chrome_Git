import time

import pytest

from pageObjects.EmployeeSearch import EmployeeSearch
from pageObjects.AddEmp_Page import AddEmployee
from pageObjects.LoginPage import loginpage
from utilities.Logger import LogGenerator
from utilities.readproperties import Readconfig


class Test_Search_Emp:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_searchEmp_005(self, setup):

        self.log.info("test_searchEmp_005 is started")

        self.driver = setup

        self.log.info("opening browser")
        self.driver.get(self.Url)
        self.log.info("Going to url-->" + self.Url)

        self.lp = loginpage(self.driver)

        time.sleep(5)

        self.lp.Enter_UserName(self.Username)
        self.log.info("Entering username-->" + self.Username)

        self.lp.Enter_Password(self.Password)
        self.log.info("Entering Password-->" + self.Password)

        time.sleep(5)

        self.lp.Click_login()
        self.log.info("Click on login button")
        self.driver.implicitly_wait(10)

        self.ae = AddEmployee(self.driver)

        self.ae.Click_PIM()
        self.log.info("Click on PIM button")

        self.es = EmployeeSearch(self.driver)

        time.sleep(3)

        self.es.Enter_EmpName("David")
        self.log.info("Entering EmpName")

        self.es.Click_SearchButton()
        self.log.info("Click on Search")

        self.driver.implicitly_wait(10)

        print(self.es.Search_Result())

        time.sleep(5)

        if self.es.Search_Result() == True:
            self.log.info("Search Found")
            self.log.info("test_searchEmp_005 is Passed")

            self.lp.Click_Menu()
            self.log.info("Click on Menu Button")

            self.lp.Click_logout()
            self.log.info("Click on logout Button")

            assert True

            self.log.info("test_searchEmp_005 is Passed")

        else:
            self.log.info("No Search Found")

            self.lp.Click_Menu()
            self.log.info("Click on MenuButton")

            self.lp.Click_logout()
            self.log.info("Click on Logout Button")

            self.log.info("test_searchEmp_005 is Failed")

            assert False
        self.driver.close()
