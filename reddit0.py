from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, keep_alive=True)

# Navigate to Reddit
driver.get("https://www.reddit.com/")

# Wait for a few seconds to observe the page
time.sleep(5)

# Close the browser
driver.quit()
