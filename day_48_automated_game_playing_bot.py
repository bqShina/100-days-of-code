from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("/Users/xiaohanqin/Development/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


def check_affordable_purchase():
    cookie_purchases = driver.find_elements(By.CSS_SELECTOR, "#store div")
    purchase_list = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    purchase_list.pop()

    purchase_prices = [int(purchase.text.split()[-1].replace(",", "")) for purchase in purchase_list]
    current_money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

    affordable_list = [price for price in purchase_prices if price <= current_money]

    if len(affordable_list) != 0:
        index = purchase_prices.index(max(affordable_list))
        return cookie_purchases[index]
    return False


timeout = time.time() + 5 * 60
print(timeout)

while time.time() <= timeout:
    check_time = time.time() + 5
    while time.time() <= check_time:
        cookie.click()
    affordable_item = check_affordable_purchase()
    if not affordable_item:
        cookie.click()
    else:
        affordable_item.click()


cookies_per_second = driver.find_element(By.ID, "cps")
print(cookies_per_second.text)
