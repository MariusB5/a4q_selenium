# Write a Python program using Selenium libraries that opens a Google Chrome browser, navigate to
# “https://www.saucedemo.com/”, enter the username ‘standard_user’ in the username textbox identified
# using relative XPath locator, enter the password ‘secret_sauce’ in the password textbox which is identified
# using CSS selector and click on the login button using ID locator. The program should then verify that the
# user is successfully logged in by verifying if the element ‘inventory_container’ is displayed using the
# classname locator.
# If the user is logged in the text ‘Login successful!’ should be displayed, if not, the text ‘Login failed!’.
# After this verification, the browser should then close.


# import unittest
# import urllib3
# import requests
# import pyautogui
# import seletools
import time
# import unittest
# from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from webdriver_manager.chrome import ChromeDriverManager


PATH = Service("C:\\Users\\marius\\chromedriver.exe")
# chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=PATH)

url = "https://amionline.net/"


driver.get(url)
time.sleep(100)
