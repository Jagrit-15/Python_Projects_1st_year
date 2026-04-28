import requests
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:
    def __init__(self):
        self.api_key = os.environ["SERPAPI_API_KEY"]

    def check_flights(self  , to_city , from_time , to_time , from_city = "CCU"):
        parameters ={
            "engine" : "google_flights",
            "departure_id": from_city,
            "arrival_id": to_city,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "gl":"in",
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "INR",
            "api_key": self.api_key,
        }
        response = requests.get(url=SERPAPI_ENDPOINT, params=parameters)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data