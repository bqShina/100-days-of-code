from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.com/Modoker-Backpack-15-6-Inch-Business-Charging/dp/B0972P3NRQ/" \
      "ref=sr_1_21?crid=2TKMFTXPPWPXT&keywords=laptop%2Bbackpack%2Bwomen&qid=1650514567" \
      "&sprefix=laptop%2Bbackpack%2B%2Caps%2C345&sr=8-21&th=1"

headers = {
    "User-Agent": "get from http://myhttpheader.com/",
    "Accept-Language": "get from http://myhttpheader.com/"
}

MY_EMAIL = "your email"
PASSWORD = "your own email password"
TARGET_PRICE = 30
# grab web element tags
response = requests.get(url=URL, headers=headers)
web_page = response.text

# scrape the product price
soup = BeautifulSoup(web_page, "lxml")

price = soup.find(name="span", class_="a-offscreen").getText()
float_price = float(price[1:])
product_title = soup.find(name="span", id="productTitle").getText().strip()

# send email alert
if float_price == TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="764762555@qq.com",
            msg=f"Subject: Amazon Price Alert!\n\n{product_title} is now {price}.\n{URL}"
        )

