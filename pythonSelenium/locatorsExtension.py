from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# this will also work but see the next line
# we can generate xpath for any element on the with its text present on it Syntax:- //tagname[text()='Text present on the element']
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()




time.sleep(5)