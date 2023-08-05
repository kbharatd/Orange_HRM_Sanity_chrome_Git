import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
# Alert(driver)
# Alert(driver).accept()
driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").click()
time.sleep(3)
driver.find_element((By.XPATH, "//a[normalize-space()='Logout']")).click()

time.sleep(3)
