from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()


driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Hi, i am Pushkar Kumar")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
