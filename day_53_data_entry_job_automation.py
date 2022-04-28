from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

RESEARCH_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22" \
               "usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-" \
               "122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22is" \
               "MapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B" \
               "%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse" \
               "%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A" \
               "%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse" \
               "%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%" \
               "22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSckkVgxmvgi5Fy4D9K93qxbUbU3lsaAHCGNZApgGTkukJ8GWg/" \
           "viewform?usp=sf_link"
CHROME_DRIVER_PATH = "/Users/xiaohanqin/Development/chromedriver"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

response = requests.get(url=RESEARCH_URL, headers=headers)
research_page = response.text

soup = BeautifulSoup(research_page, "html.parser")

addresses = soup.select(".list-card-info a address")
links = soup.select(".list-card-top a")
prices = soup.find_all(name="div", class_="list-card-price")

address_list = [address.getText() for address in addresses]
price_list = [price.getText()[0:6] for price in prices]
link_list = [link['href'] for link in links]
for i in range(len(link_list)):
    if link_list[i][0] != 'h':
        link_list[i] = "https://www.zillow.com" + link_list[i]

driver.get(FORM_URL)


def fill_form(address, price, link):
    sleep(5)
    address_field = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    price_field = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    link_field = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_field.send_keys(address)
    price_field.send_keys(price)
    link_field.send_keys(link)
    sleep(1)
    submit_btn.click()
    sleep(3)
    submit_another = driver.find_element(By.LINK_TEXT, 'Submit another response')
    submit_another.click()


for n in range(len(address_list)):
    fill_form(address_list[n], price_list[n], link_list[n])

driver.quit()
