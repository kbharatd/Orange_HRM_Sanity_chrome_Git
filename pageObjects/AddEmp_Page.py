from telnetlib import EC

from selenium.webdriver.common.by import By


class AddEmployee:
    Click_PIM_CSS_SELECTOR = (By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)")
    Click_Add_Button_XPATH = (By.XPATH, "//button[normalize-space()='Add']")
    Text_First_Name_XPATH = (By.XPATH, "//input[@placeholder='First Name']")
    Text_Middle_Name_XPATH = (By.XPATH, "//input[@placeholder='Middle Name']")
    Text_Last_Name_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")
    Click_Save_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    PersonalDetails_XPATH = (By.XPATH, "//h6[normalize-space()='Personal Details']")
    Click_Add_Emp_XPATH = (By.XPATH,"//a[normalize-space()='Add Employee']")

    def __init__(self, driver):
        self.driver = driver

    def Click_PIM(self):
        self.driver.find_element(*AddEmployee.Click_PIM_CSS_SELECTOR).click()

    def Click_Add(self):
        self.driver.find_element(*AddEmployee.Click_Add_Button_XPATH).click()

    def Enter_FirstName(self, firstname):
        self.driver.find_element(*AddEmployee.Text_First_Name_XPATH).send_keys(firstname)

    def Enter_MiddleName(self, middlename):
        self.driver.find_element(*AddEmployee.Text_Middle_Name_XPATH).send_keys(middlename)

    def Enter_LastName(self, lastname):
        self.driver.find_element(*AddEmployee.Text_Last_Name_XPATH).send_keys(lastname)

    def Click_Save(self):
        self.driver.find_element(*AddEmployee.Click_Save_Button_XPATH).click()

    def Click_AddEmployee(self):
        self.driver.find_element(*AddEmployee.Click_Add_Emp_XPATH).click()

    def AddEmp_status(self):
        try:
            self.driver.find_element(*AddEmployee.PersonalDetails_XPATH)
            return True
        except EC:
            return False
