from flight_search import FlightSearch
from flight_sheet import FlightSheet
from notification import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY_CODE = "LON"

flight_sheet = FlightSheet()
flight_search = FlightSearch()
city_data = flight_sheet.get_data()
notification = NotificationManager()
users = flight_sheet.get_users()

# print(city_data)
tomorrow = datetime.now() + timedelta(1)
next_six_month = datetime.now() + timedelta(6 * 30)

for city in city_data:
    iata_code = flight_search.iata_code(city["city"])
    # FlightSheet().edit_data(data=iata_code, object_id=city["id"])
    city_flight = flight_search.search_flight(ORIGIN_CITY_CODE, iata_code, tomorrow, next_six_month)

    if city_flight is None:
        continue

    if city["lowestPrice"] > city_flight["price"]:

        for user in users:
            notification.send_email(city_flight["price"], city_flight["departure_city"],
                                    city_flight["departure_airport"],
                                    city_flight["arrival_city"], city_flight["arrival_airport"],
                                    city_flight["date_from"], city_flight["date_to"], user["email"])




