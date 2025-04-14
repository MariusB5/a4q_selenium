# Write a Python program using Selenium libraries that opens a Google Chrome browser, navigate to
# “https://www.saucedemo.com/”, enter the username ‘standard_user’ in the username textbox identified
# using relative XPath locator, enter the password ‘secret_sauce’ in the password textbox which is identified
# using CSS selector and click on the login button using ID locator. The program should then verify that the
# user is successfully logged in by verifying if the element ‘inventory_container’ is displayed using the
# classname locator.
# If the user is logged in the text ‘Login successful!’ should be displayed, if not, the text ‘Login failed!’.
# After this verification, the browser should then close.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = Service("C:\\Users\\marius\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

url = "https://www.saucedemo.com/"
user_name = "standard_user"
password = "secret_sauce"


def login_test():
    driver.get(url)
    user_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    user_field.send_keys(user_name)
    password_field = driver.find_element(By.CSS_SELECTOR, '#password')
    password_field.send_keys(password)
    driver.find_element(By.ID, 'login-button').click()
    wait = WebDriverWait(driver, 10)
    inventory_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_container')))
    
    if inventory_container.get_attribute("id") == "inventory_container":
            print("Login successful!")
    else:
            print("Login failed!")
    
    driver.quit()


if __name__ == '__main__':
    login_test()
