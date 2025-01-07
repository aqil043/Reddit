from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, keep_alive=True)

driver.implicitly_wait(5)
driver.get("https://www.reddit.com/")

# Log in
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("Capital_Assumption22")
password_input.send_keys("w*5M#DMf*4L6DEV")
login_button2 = driver.find_element(By.XPATH, '//*[@id="login"]/auth-flow-modal/div[2]/faceplate-tracker/button')
login_button2.click()

# Wait for the page to load
time.sleep(10)

# Perform the search (if required)
search_input = driver.find_element(By.NAME, "q")
# search_input.send_keys("quality assurance")
time.sleep(3)

# Log out
# Click the profile icon to open the menu
profile_menu = driver.find_element(By.XPATH, '//*[@id="expand-user-drawer-button"]')
profile_menu.click()

# Wait for the dropdown to appear
time.sleep(2)

# Click on the "Log out" button
logout_button = driver.find_element(By.XPATH, '//*[@id="logout-list-item"]/div')
logout_button.click()

# Wait for logout to complete
time.sleep(5)

# Close the browser
driver.quit()