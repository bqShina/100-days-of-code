from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import math

CHROME_DRIVER_PATH = "Your driver path"
SIMILAR_ACCOUNT = "similar account"
USERNAME = "your username"
PASSWORD = "your password"
FOLLOWERS_PER_PANEL = 5

service = Service(CHROME_DRIVER_PATH)
driver_run = webdriver.Chrome(service=service)


class InstaFollower:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)

        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(USERNAME)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(PASSWORD)
        sleep(1)
        password_field.send_keys(Keys.ENTER)
        sleep(3)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        sleep(3)

        number_of_follower = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span'
        )
        followers_number = int(number_of_follower.text)

        follower_btn = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_btn.click()
        sleep(5)

        followers_window = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        sleep(1)

        scroll_times = math.ceil(followers_number/FOLLOWERS_PER_PANEL)
        print(scroll_times)
        for i in range(scroll_times):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                                       followers_window)
            sleep(1)

    def follow(self):
        follow_btns = self.driver.find_elements(By.CSS_SELECTOR, 'li div button')
        print(follow_btns)

        for follow_btn in follow_btns:
            try:
                follow_btn.click()
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_btn.click()
                print('cancel')
            finally:
                sleep(1)

        sleep(10)
        self.driver.quit()



instagram_follower = InstaFollower(driver=driver_run)
instagram_follower.login()
instagram_follower.find_followers()
instagram_follower.follow()
