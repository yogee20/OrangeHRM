import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

print(driver.title)

driver.maximize_window()

time.sleep(2)

username = driver.find_element(By.XPATH, "//*[@name='username']").send_keys('Admin')

time.sleep(2)

password=driver.find_element(By.XPATH, "//input[@type='password']").send_keys('admin123')

time.sleep(3)

logIn=driver.find_element(By.XPATH, "//*[@type='submit']").click()

time.sleep(2)

search = driver.find_element(By.XPATH, "//*[@class='oxd-input oxd-input--active']")

time.sleep(2)

search_Performance = driver.find_element(By.XPATH, "//*[@class='oxd-input oxd-input--active']").send_keys("Performance")

time.sleep(2)

click_on_perf = driver.find_element(By.XPATH, "//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name']").click()

time.sleep(2)
