import requests_cache
from pprint import pprint
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# Here we are not caching anything ending in *.sheety.co
# everything else is cached for 1 hour (3600 seconds). 

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

notification_manager = NotificationManager()

# going and returning time 
tomorrow = datetime.now() + timedelta(days=1)
one_months = datetime.now() + timedelta(days=30)

# searching relevant flights 
flight_search = FlightSearch()

# searching for all the destination stored in the google sheet 
for destination in sheet_data:
    print(f"Getting Flights for {destination['city']}")

    flight_data = flight_search.check_flights(destination["iataCode"] ,tomorrow , one_months)

    # finding the cheapest flight 
    cheapest_flight = find_cheapest_flight(flight_data , return_date=one_months.strftime("%Y-%m-%d"))
    pprint(f"{cheapest_flight.destination_airport}: INR {cheapest_flight.price}")

    # updating data in sheet and sending message if the flight is cheaper than the lowest value stored 
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)

        notification_manager.send_sms(
            message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )

        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only INR {cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )