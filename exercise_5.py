# Same as exercise 4 but now the password field will be located using friendly locator.
# First the textbox for the username needs to be found using the id locator then the browser will find the
# input tag element just below the username textbox to enter the password.


# library imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = Service("C:\\Users\\marius\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

url = "https://www.saucedemo.com/"
user_name = "standard_user"
password = "secret_sauce"


def login_to_saucedemo():
    try:
        driver.get(url)
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
    
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}")
    
    finally:
        driver.quit()


if __name__ == '__main__':
        login_to_saucedemo()
