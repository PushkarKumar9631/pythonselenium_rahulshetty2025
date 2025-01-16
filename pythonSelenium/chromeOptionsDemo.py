from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions() ## calling Chrome Options
chrome_options.add_argument("--start-maximized") # for starting as maximized window
chrome_options.add_argument("headless") # for invoking browser in background
chrome_options.add_argument("--ignore-certificate-errors") # for ignoring private connection error

# driver = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application", options=chrome_options)
# this above executable path has been removed from the selenium 4 version and has been replaced with service
# class so use service class as below

service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options= chrome_options)  ## here passed chrome option object to driver
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice")
print(driver.title)