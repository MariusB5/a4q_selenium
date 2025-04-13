# Write a Python program using Selenium libraries that opens a Google Chrome browser,
# navigate to “https://www.saucedemo.com/” and closes the browser.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


PATH = Service("C:\\Users\\marius\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

url = "https://www.saucedemo.com/"


driver.get(url)
driver.quit()
