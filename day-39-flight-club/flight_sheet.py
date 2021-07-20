import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

headers = {
    "Authorization": f"Basic {os.getenv('SHEET_KEY')}"
}


class FlightSheet:
    def __init__(self):
        self.end_point = SHEET_ENDPOINT
        self.headers = headers
        self.body = {
            "price": {}
        }

    def get_data(self):
        response = requests.get(url=self.end_point, headers=self.headers)
        return response.json()["prices"]

    def edit_data(self, data, object_id):
        body = {
            "price": {
                "iataCode": data
            }
        }
        requests.put(url=f"{self.end_point}/{object_id}", json=body, headers=self.headers)




