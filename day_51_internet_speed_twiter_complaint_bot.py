from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

PROMISED_DOWN = 20
PROMISED_UP = 2
CHROM_DRIVER_PATH = "your chrom driver path"
TWITTER_EMAIL = "your twitter email"
TWITTER_USERNAME = "your username"
TWITTER_PASSWORD = "your password"

service = Service(CHROM_DRIVER_PATH)
driver_run = webdriver.Chrome(service=service)


class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.driver = driver
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        go_btn = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        )
        go_btn.click()
        sleep(60)
        download = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
            'div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        )
        self.down = float(download.text)
        print(f"down: {self.down}")
        upload = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
            'div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
        )
        self.up = float(upload.text)
        print(f"up: {self.up}")
        sleep(2)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            def fill_password():
                password_field = self.driver.find_element(By.NAME, "password")
                password_field.send_keys(TWITTER_PASSWORD)
                sleep(1)

            self.driver.get("https://twitter.com/")
            sleep(3)
            # log in on tweet
            sign_in = self.driver.find_element(By.LINK_TEXT, "Sign in")
            sign_in.click()
            sleep(3)

            email_label = self.driver.find_element(
                By.XPATH,
                '//label[@class="css-1dbjc4n r-1ets6dv r-z2wwpe r-rs99b7 r-18u37iz"]'
            )
            email_label.click()
            sleep(1)

            email_field = self.driver.find_element(By.NAME, "text")
            email_field.send_keys(TWITTER_EMAIL)
            email_next = self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div'
            )
            email_next.click()
            sleep(2)

            try:
                fill_password()
            except NoSuchElementException:
                username_field = self.driver.find_element(By.XPATH, '//input[@name="text"]')
                username_field.send_keys(TWITTER_USERNAME)
                username_next = self.driver.find_element(
                    By.XPATH,
                    '//div[@class="css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr '
                    'r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]'
                )
                username_next.click()
                sleep(2)

                fill_password()

            log_in = self.driver.find_element(
                By.XPATH,
                '//div[@class="css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox '
                'r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]'
            )
            log_in.click()
            sleep(3)

            # post a tweet
            post_label = self.driver.find_element(
                By.XPATH,
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/'
                'div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/'
                'label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            post_label.click()
            sleep(1)

            post_field = self.driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/'
                          'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div'
                          '/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]'
                          '/div/div/div/div/span'
            )
            post_field.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up} when I pay for "
                                 f"{PROMISED_DOWN}down/{PROMISED_UP}up?")

            tweet_btn = self.driver.find_element(
                By.XPATH,
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/'
                'div/div/div[2]/div[3]/div/div/div[2]/div[3]'
            )
            tweet_btn.click()
            sleep(8)
        else:
            print("Awesome Internet!")
        self.driver.quit()
        

internet_twitter_bot = InternetSpeedTwitterBot(driver=driver_run)

internet_twitter_bot.get_internet_speed()
internet_twitter_bot.tweet_at_provider()
