import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MY_LAT = -37.813629
MY_LONG = 144.963058
api_key = os.environ.get("OWN_API_KEY")
account_sid = "ACaadf9111bfb3fdea387401c29eca8c31"
auth_token = os.environ.get("AUTH_TOKEN")
will_rain = False

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"]
# print(weather_data[0]["weather"][0]["id"])

weather_id_list = {hour: weather_data[hour]["weather"][0]["id"] for hour in range(0, 12)}
# print(type(weather_id_list[0]))
for hour in weather_id_list:
    if weather_id_list[hour] < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                    .create(
                            body="It's going to rain today. Remember to bring an ☂️",
                            from_='+19712022892',
                            to='+61404610849'
                        )
    print(message.status)

