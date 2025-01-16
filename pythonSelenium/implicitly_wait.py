import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5) # if i remove this wait then this code will fail at line 30 because selenium try to find that
# element immediately and it will not be able to find so it fails

#NOTE:- implicit wait will wait to max 5 seconds for findind any element, and if the element is found at 2 seconds it will
# the rest 3 seconds and execute the code

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ca")
time.sleep(2) ## i did not removed this sleep because selenium implicit wait will not work if the return value is LIST
## and in the below line implicit wait will not work, the only exception which implcit wait cannot handle, so we need
## hard wait time.sleep(2) for getting the expected results
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
print(count)

## for adding each element to the cart
for result in results:
    result.find_element(By.XPATH, "div/button").click()  ##  here we are chaining the result from results web
    # elements thats why half x path is written here and we are finding element with not driver,find_element but with
    # result.find_element directly

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)