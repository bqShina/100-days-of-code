from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


class NotificationManager:

    def __init__(self):
        self.account_sid = ACCOUNT_SID
        self.auth_token = AUTH_TOKEN
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, price, departure_city, departure_lata_code, arrival_city,
                     arrival_lata_code, date_from, date_end):
        message = self.client.messages \
                        .create(
                             body=f"Low price alert! Only £{price} to fly from {departure_city}-{departure_lata_code} "
                                  f"to {arrival_city}-{arrival_lata_code}, from {date_from[:10]} to {date_end[:10]}.",
                             from_=os.getenv("PHONE_FROM"),
                             to=os.getenv("PHONE_TO")
                         )
        print(message.status)


