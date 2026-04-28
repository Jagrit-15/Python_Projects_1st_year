import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# loading environment data
load_dotenv()

# API 
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/fb73cb28beaabe1db9a08b13e8917b2b/flightDeals/sheet1"

class DataManager:

    def __init__(self):
        self.user = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}

    # getting the city name iata value and lowest price 
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT , auth=self.authorization)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data
       
    # updating the lowest price 
    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "sheet1": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            auth=self.authorization
        )