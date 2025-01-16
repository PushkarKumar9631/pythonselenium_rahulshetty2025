from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise")
#Dyanamic dropdown selection using select class locator

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if "india" == country.text.lower():  #.lower is used to make the code independent from case sensitivity
        # but the main method to grab text is .text only
        country.click()
        break
#print(driver.find_element(By.ID, "autosuggest").text) # .text method is used for extracting static value
assert driver.find_element(By.ID, "autosuggest").get_attribute("value").lower() == "india" #.get_attribute is used for extracting
# dyanamically entered value in any drop down or entered field

time.sleep(2)
