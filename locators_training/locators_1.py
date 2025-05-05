from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

file_path = "file:///C:/Users/marius/a4q_selenium/locators_training/locators_1.html"


driver.get(file_path)
time.sleep(5)
