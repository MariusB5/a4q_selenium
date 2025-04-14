# Same as exercise 5 but now the automation solution need to wait for the page to completely load before
# starting to starting to enter the username and password. If the page does not load within 180s then the
# automation test should continue.
# The page status need to be scanned to check if the page is ready or not.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


PATH = Service("C:\\Users\\marius\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

url = "https://www.saucedemo.com/"
user_name = "standard_user"
password = "secret_sauce"


def login_to_saucedemo():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            driver.get(url)
            WebDriverWait(driver, 180).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#root > div > div.login_logo')))
            user_field = driver.find_element(By.ID, 'user-name')
            user_field.send_keys(user_name)
            password_field = driver.find_element(locate_with(By.TAG_NAME, 'input').below({By.ID:'user-name'}))  # overcomplicated way to locate an element
            password_field.send_keys(password)
            driver.find_element(By.ID, 'login-button').click()
            wait = WebDriverWait(driver, 5)
            inventory_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_container')))
            if inventory_container.get_attribute("id") == "inventory_container":
                    print("Login successful!")
            else:
                    print("Login failed!")
        else:
            print("Web page not loaded.")
    
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}")
    
    finally:
        driver.quit()


if __name__ == '__main__':
        login_to_saucedemo()
