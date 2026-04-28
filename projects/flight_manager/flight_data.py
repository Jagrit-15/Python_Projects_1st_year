class FlightData:

    def __init__(self , price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(data , return_date):
    # Handle empty data if no flight data is returned
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    
    # combining all the flights to loop through it 
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    cheapest_flight = None
    lowest_price = None

    for flight in all_flights:

        try:
            price = flight["price"]
        except(KeyError):
            continue
        else:
            if lowest_price is None or price < lowest_price:
                lowest_price = price
                origin = flight["flights"][0]["departure_airport"]["id"] # storing the value of departure airport iata
                destination = flight["flights"][-1]["arrival_airport"]["id"] # -1 because it can have connected flights, to store the final destination
                out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0] # removing time
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date) # storing as cheapest

    # If no flight had a price at all
    if cheapest_flight is None:
        print("No flights with valid price found.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    return cheapest_flight