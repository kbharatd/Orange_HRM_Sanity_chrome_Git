import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.ChromeOptions(options=chrome_options)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(5)
    return driver


def pytest_metadata(metadata):
    metadata["Environment"] = "Test"
    metadata["Project Name"] = "OrangeHRM"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "Credence"


@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("Admin1", "admin123", "Fail"),
    ("Admin", "admin1234", "Fail"),
    ("Admin1", "admin1234", "Fail")
])
def getDataforlogin(request):
    return request.param
