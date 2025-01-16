from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

### here we are checking if the Sorting on the website is working or not

driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()
veggieList = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")

expectedveggies = []
for veggies in veggieList:
    expectedveggies.append(veggies.text)

print(expectedveggies)

sortedVeggies = sorted(expectedveggies)
print(sortedVeggies)

assert sortedVeggies == expectedveggies


