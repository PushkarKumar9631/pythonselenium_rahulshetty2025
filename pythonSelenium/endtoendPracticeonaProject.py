## in this project i will automate a website and learn end to end all methods of selenium

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")



service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options= chrome_options)
driver.implicitly_wait(5)