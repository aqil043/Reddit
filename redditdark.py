from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, keep_alive=True)

driver.implicitly_wait(5)
driver.get("https://www.reddit.com/")

# Login process
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("Capital_Assumption22")
password_input.send_keys("w*5M#DMf*4L6DEV")
login_button2 = driver.find_element(By.XPATH, '//*[@id="login"]/auth-flow-modal/div[2]/faceplate-tracker/button')
login_button2.click()

# Wait for login to complete
time.sleep(10)

# Navigate to Settings (Click the profile menu)
profile_menu = driver.find_element(By.XPATH, '//*[@id="expand-user-drawer-button"]')
profile_menu.click()

# Wait for the dropdown to appear
time.sleep(2)


# Navigate to the dark mode toggle button
# Find the dark mode switch by its class name (you can adjust the class name if necessary)
dark_mode_switch = driver.find_element(By.CLASS_NAME, "switch-input-primary")

# Click the dark mode toggle to enable dark mode
dark_mode_switch.click()

# Wait for changes to take effect (Optional)
time.sleep(3)

# You can continue with your script or log out if needed
