import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")  # use double back slashes to avoid
#escape sequence warning from python for example
# service_obj = Service("F:\\selenium_drivers\\chromedriver-win64\\chromedriver.exe") or r as prefix
# for example service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")


driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()
driver.implicitly_wait(5)

action = ActionChains(driver)

# action.click_and_hold(driver.find_element(By.CSS_SELECTOR, "css path"))
# action.drag_and_drop()
# action.double_click()
# action.context_click()  ## this is used to right click on some element
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()






time.sleep(3)