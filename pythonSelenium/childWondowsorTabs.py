import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"F:\selenium_drivers\firefox\geckodriver.exe")

driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
message = driver.find_element(By.CSS_SELECTOR, "h3").text
assert message == "New Window"

driver.quit()