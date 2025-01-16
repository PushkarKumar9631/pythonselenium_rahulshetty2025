import time
from selenium import webdriver
# from selenium.webdriver.ie.service import Service # we need to use service package for manually invoking chrome

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com")

driver.maximize_window()
print(driver.title)
print(driver.current_url)

## we can also invoke chrome using service method
# we use this method when webdriver.Chrome() is unable to handle and there are some cases where companies uses proxies
# Syntax

# service_obj = Service("F:\selenium_drivers\chromedriver-win64\chromedriver.exe") # use double back slashes to avoid
# #escape sequence warning from python for example
# # service_obj = Service("F:\\selenium_drivers\\chromedriver-win64\\chromedriver.exe") or r as prefix
# # for example service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://rahulshettyacademy.com")








time.sleep(5)