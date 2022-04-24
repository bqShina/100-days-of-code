from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


USER_NAME = "your user name"
PASSWORD = "your password"
PHONE = "your phone number"

service = Service("/Users/xiaohanqin/Development/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&geoId=100992797&"
           "keywords=web%20developer&location=Melbourne%2C%20Victoria%2C%20Australia")
time.sleep(1)
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

time.sleep(5)

user_account = driver.find_element(By.NAME, "session_key")
user_account.send_keys(USER_NAME)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)


def close_application():
    close_btn = driver.find_element(By.CSS_SELECTOR, "button.artdeco-modal__dismiss")
    close_btn.click()


def apply_job():
    try:
        easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        easy_apply.click()
        time.sleep(3)
        phone_number_field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')

        if phone_number_field.get_attribute("value") == "":
            phone_number_field.send_keys(PHONE)

        submit_application = driver.find_element(By.CSS_SELECTOR, "footer .artdeco-button")
        if submit_application.get_attribute("aria-label") == "Submit application":
            submit_application.click()
            close_application()
            print("applied")
        else:
            close_application()
            time.sleep(2)
            discard = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button")
            discard.click()
            print("skipped")
        time.sleep(5)
    except NoSuchElementException:
        pass


time.sleep(1)

all_jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for job in all_jobs:

    job.click()
    time.sleep(5)
    apply_job()

time.sleep(5)
driver.quit()
