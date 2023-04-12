import time

from select import select
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

print(driver.title)

driver.maximize_window()

time.sleep(2)

username=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')

time.sleep(2)

password=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')

time.sleep(2)

logIn=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

time.sleep(2)

clickOnAdmin=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()

time.sleep(2)

add_user = driver.find_element(By.XPATH, "//*[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()

time.sleep(2)

user_role= driver.find_element(By.XPATH, "//*[@class='oxd-select-text oxd-select-text--active'][1]").click()




# select_admin = driver.find_element(By.XPATH, "//*[text()='Admin']").click()
#
# time.sleep(2)