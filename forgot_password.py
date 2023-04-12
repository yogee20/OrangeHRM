import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

print(driver.title)

driver.maximize_window()

time.sleep(2)

forgotPassword=driver.find_element(By.XPATH,"//*[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()

time.sleep(2)