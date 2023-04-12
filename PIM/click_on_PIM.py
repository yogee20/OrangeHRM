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

time.sleep(1)

Click_on_PIM=driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span").click()

time.sleep(1)

add= driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button/i").click()

time.sleep(1)

emp_first_name = driver.find_element(By.XPATH, "//*[@name='firstName']").send_keys("Abhay")

time.sleep(2)

emp_mid_name = driver.find_element(By.XPATH, "//*[@name='middleName']").send_keys("Abhay")

time.sleep(2)

emp_last_name = driver.find_element(By.XPATH, "//*[@name='lastName']").send_keys("Abhay")

time.sleep(2)

emp_id= driver.find_element(By.XPATH, "(//*[@class='oxd-input oxd-input--active'])[2]").send_keys("1234")

time.sleep(2)

save_ = driver.find_element(By.XPATH, "//*[@type='submit']").click()

time.sleep(2)