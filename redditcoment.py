from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, keep_alive=True)

driver.implicitly_wait(10)  # Hər bir elementin tapılması üçün 10 saniyəlik gözləmə

# Reddit səhifəsinə getmək
driver.get("https://www.reddit.com/r/europe/comments/1hu4lp2/tech_made_in_europe_the_machine_that_makes_the/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button")

# Giriş (Login)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("Capital_Assumption22")  # Burada istifadəçi adınızı daxil edin
password_input.send_keys("w*5M#DMf*4L6DEV")  # Burada şifrənizi daxil edin
login_button2 = driver.find_element(By.XPATH, '//*[@id="login"]/auth-flow-modal/div[2]/faceplate-tracker/button')
login_button2.click()

# Sayfanın tamamilə yüklənməsini gözləyirik
time.sleep(10)  # Login edildikdən sonra səhifənin tamamilə yüklənməsini gözləyin

# Şərh qutusunun görünməsini gözləyirik
try:
    # Şərh qutusunu tapmaq üçün gözləyirik
    comment_box_xpath = "//div[@class='DraftEditor-editorContainer']//p"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, comment_box_xpath))
    )

    # Şərh qutusuna klikləyirik (çünki bəzən şərh sahəsi əvvəlcə tıklanmalı olur)
    comment_box = driver.find_element(By.XPATH, comment_box_xpath)
    comment_box.click()

    # Şərh yazırıq
    comment_box.send_keys("6 QA-dən salamlar")

    # Şərhi göndəririk (RETURN düyməsini basırıq)
    comment_box.send_keys(Keys.RETURN)
    
    # Şərhin göndərilməsini gözləyirik
    time.sleep(5)

except Exception as e:
    print(f"Bir xətaya rast gəlinib: {e}")

# Əlavə olaraq, istifadəçi çıxışı (logout) etmək istəsəniz:
profile_menu = driver.find_element(By.XPATH, '//*[@id="expand-user-drawer-button"]')
profile_menu.click()

# Dropdownun açılmasını gözləyirik
time.sleep(2)

# Çıxış düyməsini tapırıq və basırıq
logout_button = driver.find_element(By.XPATH, '//*[@id="logout-list-item"]/div')
logout_button.click()

# Çıxışın tamamlanmasını gözləyirik
time.sleep(5)

# Brauzeri bağlayırıq
driver.quit()
