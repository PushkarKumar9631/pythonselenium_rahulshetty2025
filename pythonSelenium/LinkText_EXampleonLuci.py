# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome()
#
# driver.get("https://lucimoments.com")
# driver.find_element(By.LINK_TEXT, "Forgot password ?").click()
#
#
#
#
#
#
#
# time.sleep(5)

# not working in Link Text method, need to use different method for the same

# it worked using xpath

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://lucimoments.com")
driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1n9plek']").click()






time.sleep(5)