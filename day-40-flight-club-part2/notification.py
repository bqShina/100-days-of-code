from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = "bqshina1994@gmail.com"
password = os.getenv("PASSWORD")

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


class NotificationManager:

    def __init__(self):
        self.account_sid = ACCOUNT_SID
        self.auth_token = AUTH_TOKEN
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, price, departure_city, departure_lata_code, arrival_city,
                     arrival_lata_code, date_from, date_end):
        # message = self.client.messages \
        #                 .create(
        #                      body=f"Low price alert! Only £{price} to fly from {departure_city}-{departure_lata_code} "
        #                           f"to {arrival_city}-{arrival_lata_code}, from {date_from[:10]} to {date_end[:10]}.",
        #                      from_=os.getenv("PHONE_FROM"),
        #                      to=os.getenv("PHONE_TO")
        #                  )
        # print(message.status)
        print(f"Low price alert! Only £{price} to fly from {departure_city}-{departure_lata_code} "
              f"to {arrival_city}-{arrival_lata_code}, from {date_from} to {date_end}.")

    def send_email(self, price, departure_city, departure_airport, arrival_city,
                   arrival_airport, date_from, date_to, email):
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject: New Low Price Flight!\n\n"
                                f"Low price flight! Only £{price} to fly from {departure_city}-"
                                f"{departure_airport} to {arrival_city}-{arrival_airport}, from {date_from} to {date_to}."
                                f"\nhttps://www.google.co.uk/flights?hl=en#flt={departure_airport}.{arrival_airport}."
                                f"{date_from}*{arrival_airport}.{departure_airport}.{date_to}".encode('utf-8'))
        connection.close()


