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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options,keep_alive=True)

driver.implicitly_wait(5)
driver.get("https://www.reddit.com/")
login_button=driver.find_element(By.ID,"login-button")
# print(login_button.text)
login_button.click()
username_input=driver.find_element(By.NAME,"username")
password_input=driver.find_element(By.NAME,"password")
username_input.send_keys("Capital_Assumption22")
password_input.send_keys("w*5M#DMf*4L6DEV")
login_button2=driver.find_element(By.XPATH,'//*[@id="login"]/auth-flow-modal/div[2]/faceplate-tracker/button')
# print(login_button2.text)
login_button2.click()
time.sleep(10)
search_input=driver.find_element(By.NAME,"q")
# print(search_input.text)
# search_input.send_keys("quality assurance")

time.sleep(3)