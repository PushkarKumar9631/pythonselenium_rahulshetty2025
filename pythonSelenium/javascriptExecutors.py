import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions() # here calling the webdriver class
chrome_options.add_argument("headless") ## this will run our automation code in background
chrome_options.add_argument("--ignore-certification-errors") # for handling error pages which asks for private connection


service_obj = Service(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scroll(0,document.body.scrollHeight);")


