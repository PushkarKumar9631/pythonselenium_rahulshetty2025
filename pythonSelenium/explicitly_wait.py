import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ca")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
print(count)

## assignment 2 :- create a expected list and compare with the extracted list of items from the search

# expectedList = ["Cauliflower - 1 Kg", "Carrot - 1 Kg", "Capsicum", "Cashews - 1 Kg"]
# actualList = []
#
# for result in results:
#     actualList.append(result.find_element(By.XPATH, "h4").text)
#
# assert expectedList == actualList    # this will fail when the search keyword will be failed
########################## assignment 2 ended here #################

## for adding each element to the cart
for result in results:
    result.find_element(By.XPATH, "div/button").click()  ##  here we are chaining the result from results web
    # elements thats why half x path is written here and we are finding element with not driver,find_element but with
    # result.find_element directly

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)  # asks to argument and note that the WebDriverWait has all capital letters
# starting word and also we need to import package to use expected conditions in below line
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)


## Sum of a cart value and compare with the total amount

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount

# assigntment 1 :- put assertion condition to check whether the discounted amount is always lesser than the total amount

# wait2 = WebDriverWait(driver, 8)
# wait2.until(expected_conditions.presence_of_element_located())

discountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalAmount > discountAmount
print("discount is less than total")



