from flight_search import FlightSearch
from flight_sheet import FlightSheet
from notification import NotificationManager

flight_sheet = FlightSheet()
flight_search = FlightSearch()
city_data = flight_sheet.get_data()
notification = NotificationManager()
# print(city_data)

for city in city_data:
    iata_code = flight_search.iata_code(city["city"])
    # FlightSheet().edit_data(data=iata_code, object_id=city["id"])
    city_flight = flight_search.search_flight(iata_code)
    if city["lowestPrice"] > city_flight["price"]:
        notification.send_message(city_flight["price"], city_flight["departure_city"],
                                  city_flight["departure_iata_code"],
                                  city_flight["arrival_city"], city_flight["arrival_iata_code"],
                                  city_flight["date_from"], city_flight["date_end"])




