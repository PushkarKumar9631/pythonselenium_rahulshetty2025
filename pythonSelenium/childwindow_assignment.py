# max time 15 minutes

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windowOpened = driver.window_handles
driver.switch_to.window(windowOpened[1])
sentance = driver.find_element(By.XPATH, "//div/p[@class='im-para red']").text
email_obj = sentance[18:49]
print(email_obj)

driver.switch_to.window(windowOpened[0])
driver.find_element(By.NAME, "username").send_keys(email_obj)
driver.find_element(By.NAME, "password").send_keys("12345")
driver.find_element(By.NAME, "terms").click()
driver.find_element(By.NAME, "signin").click()

wait = WebDriverWait(driver, 10)
errormessage_element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-danger col-md-12']")))
errormessage = errormessage_element.text
print(errormessage)

