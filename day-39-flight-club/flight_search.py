import requests
import os
from dotenv import load_dotenv

load_dotenv()
KIWI_ENDPOINT = os.getenv("KIWI_ENDPOINT")
KIWI_KEY = os.getenv("KIWI_KEY")

headers = {
    "apiKey": KIWI_KEY
}


class FlightSearch:
    def __init__(self):
        self.endpoint = KIWI_ENDPOINT
        self.headers = headers

    def iata_code(self, city):
        param = {
            "term": city
        }
        response = requests.get(url=f"{self.endpoint}/locations/query", params=param, headers=self.headers)
        return response.json()["locations"][0]["code"]

    def search_flight(self, city_code):
        param = {
            "fly_from": "LON",
            "fly_to": city_code,
            "date_from": "19/07/2021",
            "date_to": "19/01/2022",
        }
        response = requests.get(url=f"{self.endpoint}/v2/search", params=param, headers=self.headers)
        flight_data = response.json()["data"]

        lowest_price = 9999
        departure_city = ""
        departure_iata_code = ""
        arrival_city = ""
        arrival_iata_code = ""
        date_from = ""
        date_end = ""
        for flight in flight_data:
            dict_flight = {
                "city_from": flight["cityFrom"],
                "fly_code_from": flight["flyFrom"],
                "city_to": flight["cityTo"],
                "fly_code_to": flight["flyTo"],
                "price": int(flight["price"]),
                "date_from": flight["local_departure"],
                "arrival_date": flight["local_arrival"]
            }
            if dict_flight["price"] < lowest_price:
                lowest_price = dict_flight["price"]
                departure_city = dict_flight["city_from"]
                departure_iata_code = dict_flight["fly_code_from"]
                arrival_city = dict_flight["city_to"]
                arrival_iata_code = dict_flight["fly_code_to"]
                date_from = dict_flight["date_from"]
                date_end = dict_flight["arrival_date"]
        return {
            "price": lowest_price,
            "departure_city": departure_city,
            "departure_iata_code": departure_iata_code,
            "arrival_city": arrival_city,
            "arrival_iata_code": arrival_iata_code,
            "date_from": date_from,
            "date_end": date_end
        }
