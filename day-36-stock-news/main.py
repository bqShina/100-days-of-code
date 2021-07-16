import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = "*********"
stock_url = "https://www.alphavantage.co/query"

news_api_key = "*********"
news_url = "https://newsapi.org/v2/everything"

account_sid = "*********"
auth_token = "*********"


def get_news():
    news_parameters = {
        "apiKey": news_api_key,
        "q": COMPANY_NAME,
        # "language": "en",
    }
    news_response = requests.get(url=news_url, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    return news_data


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}

response = requests.get(url=stock_url, params=parameters)
response.raise_for_status()
stock_price_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_price_data.items()]
# print(data_list)
yesterday_close = float(data_list[0]["4. close"])
before_yesterday_close = float(data_list[1]["4. close"])

stock_price_change = (yesterday_close - before_yesterday_close) / yesterday_close
print(stock_price_change)

if stock_price_change >= 0.05 or stock_price_change <= -0.05:
# if stock_price_change > -0.05:
    news = get_news()
    print(news)
    stock_percent = '{:.0%}'.format(stock_price_change)
    up_down = ""
    if stock_price_change > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    client = Client(account_sid, auth_token)
    news_content = [f"{STOCK}: {up_down}{stock_percent}\nHeadline: {article['title']}\n" \
                    f"Brief: {article['description']}\n" for article in news]
    for news in news_content:
        message = client.messages \
                        .create(
                             body=news,
                             from_='+19712022892',
                             to='+61404610849'
                         )

        print(message.status)


