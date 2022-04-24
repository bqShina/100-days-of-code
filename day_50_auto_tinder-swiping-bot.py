from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

USER_NAME = "your username"
PASSWORD = "your password"

service = Service("/Users/xiaohanqin/Development/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://tinder.com/")

time.sleep(2)
log_in = driver.find_element(
    By.XPATH,
    '//*[@id="q939012387"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
)
log_in.click()

time.sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys(USER_NAME)
password_field = driver.find_element(By.NAME, "pass")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(3)
location_allow = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location_allow.click()
time.sleep(3)
no_notification = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
no_notification.click()
time.sleep(3)
accept_cookie = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
accept_cookie.click()

time.sleep(5)

for n in range(100):
    try:
        like_button = driver.find_element(
            By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
        )
        like_button.click()
        print("liked")
        time.sleep(1)
    except ElementClickInterceptedException:
        back_button = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a')
        back_button.click()
        time.sleep(1)
    except NoSuchElementException:
        time.sleep(2)

driver.quit()
