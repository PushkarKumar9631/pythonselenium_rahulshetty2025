import os.path
from datetime import datetime
from fileinput import filename

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service


chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("Headless")

service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_option )
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()  ## here '*' star symbol used as regular expression
# for fetching the element with only partial value.
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

#//div[@class='card h-100']/div/h4/a
#product =//div[@class='card h-100']
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        #Add item into cart
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successText


# fileName = "screen2.png" ## this is for simple naming, now for dyanamic file naming use below line

file_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png" #this will generate dyanamic filename using timedate
file_path = os.path.join(r"F:\Rahul_shetty_Python_selenium\pythonSelenium\screenshots", file_name)

if driver.get_screenshot_as_file(file_path):
    print(f"Screenshot successfully saved at: {file_path}")
else:
    print("Failed to save the screenshot.")

