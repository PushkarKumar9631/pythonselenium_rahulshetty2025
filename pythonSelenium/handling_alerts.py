import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Pushkar"

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert # we use switch to method to go from browser mode to any other mode
alerttext = alert.text # here i am reading the text from the alert
print(alerttext)
assert name in alerttext
alert.accept() # accept is used to give the alert positive and to press ok

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alert.dismiss() # dismiss is used to give the alert the negative message or cancel


time.sleep(4)