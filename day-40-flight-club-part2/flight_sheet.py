import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
USER_ENDPOINT = os.getenv("USERS_ENDPOINT")

headers = {
    "Authorization": f"Basic {os.getenv('SHEET_KEY')}"
}


class FlightSheet:
    def __init__(self):
        self.data_obtained = {}

    def get_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=headers)
        self.data_obtained = response.json()["prices"]
        return self.data_obtained

    def edit_data(self, data, object_id):
        body = {
            "price": {
                "iataCode": data
            }
        }
        requests.put(url=f"{SHEET_ENDPOINT}/{object_id}", json=body, headers=headers)

    def get_users(self):
        response = requests.get(url=USER_ENDPOINT, headers=headers)
        self.data_obtained = response.json()["users"]
        return self.data_obtained




