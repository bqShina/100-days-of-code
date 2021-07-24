import requests
import os
from dotenv import load_dotenv
from pprint import pprint

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

    def search_flight(self, orgin_city_code, city_code, from_date, to_date):
        param = {
            "fly_from": orgin_city_code,
            "fly_to": city_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{self.endpoint}/v2/search", params=param, headers=self.headers)
        try:
            flight_data = response.json()["data"][0]
            # pprint(flight_data)
        except IndexError:
            try:
                param["max_stopovers"] = 1
                response = requests.get(url=f"{self.endpoint}/v2/search", params=param, headers=self.headers)
                stops_over_flight = response.json()["data"][0]
            except IndexError:
                print("Really no flights available")
                return None
            else:
                cheap_flight = {
                    "price": int(stops_over_flight["price"]),
                    "departure_city": stops_over_flight["route"][0]["cityFrom"],
                    "departure_airport": stops_over_flight["route"][0]["flyFrom"],
                    "arrival_city": stops_over_flight["route"][2]["cityTo"],
                    "arrival_airport": stops_over_flight["route"][2]["flyTo"],
                    "date_from": stops_over_flight["route"][0]["local_departure"][:10],
                    "date_to": stops_over_flight["route"][2]["local_departure"][:10],
                    "stop_over": 1,
                    "via_city": stops_over_flight["route"][1]["cityTo"]
                }
                return cheap_flight

        else:
            cheap_flight = {
                "price": int(flight_data["price"]),
                "departure_city": flight_data["route"][0]["cityFrom"],
                "departure_airport": flight_data["route"][0]["flyFrom"],
                "arrival_city": flight_data["route"][0]["cityTo"],
                "arrival_airport": flight_data["route"][0]["flyTo"],
                "date_from": flight_data["route"][0]["local_departure"][:10],
                "date_to": flight_data["route"][1]["local_departure"][:10]
            }
            return cheap_flight
