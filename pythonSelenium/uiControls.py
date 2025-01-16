import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

## marking Check boxes

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value").lower() == "option2":
        checkbox.click()
        assert checkbox.is_selected() # this line of code will be verify that the checkbox is selected or not
        break


## Selecting radio buttons

radioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radio_btn in radioButtons:
    if radio_btn.get_attribute("value").lower() == "radio3":
        radio_btn.click()
        assert radio_btn.is_selected()
        break
## if button places are fixed then we can also use this below code
# radioButtons = driver.find_elements(By.CSS_SELECTOR, "radioButton']")
# radioButtons[2].click
# assert radioButtons[2].is_selected()

# to check something is displayed or not
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
#assert driver.find_element(By.ID, "displayed-text").is_displayed() # to check after hiding that element

time.sleep(3)
