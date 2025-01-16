
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Locators are the element finders on any page, which can be :- ID, Xpath, CSS Selector, Class Name, name, link text etc.

driver.find_element(By.NAME, "email").send_keys("pushkarkumar84332@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("@Testtest1")
driver.find_element(By.ID, "exampleCheck1").click()

# Element selecion using X path
# Syntax:-    //tagname[@attribute='value'] -> for example, xpath for submit button on this
# page will be //input[@type='submit']

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
driver.find_element(By.XPATH, "(//input[@type='text']) [3]").send_keys("Hello Again")
driver.find_element(By.XPATH,"(//input[@type='text']) [3]").clear()
print(message)
assert "success" in message

# Element selecion using Css Selector
# Syntax:-    tagname[attribute='value'] -> for example, Css for submit button on this
# page will be input[type='submit']
# Css selectors can also be defined as #ID or .classname

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Pushkar Kumar")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()


time.sleep(5)