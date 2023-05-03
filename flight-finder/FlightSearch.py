from dotenv import load_dotenv
import os 
import requests 
from FlightData import FlightData

load_dotenv()

# -------- TEQUILA -------- #
TEQUILA_ENDPOINT = os.environ["TEQUILA_ENDPOINT"]
TEQUILA_AP_KEY = os.environ["TEQUILA_AP_KEY"]

class FlightSearch:

    def __init__(self):
        pass

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apiKey": TEQUILA_AP_KEY}
        query =  {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        #print(f"Code: {code}")
        return code
        pass

    def find_flight(self, fly_from_code, fly_to_code, from_date, to_date):
        location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apiKey": TEQUILA_AP_KEY}
        query =  {"fly_from": fly_from_code, 
              "fly_to": fly_to_code, 
              "date_from": from_date.strftime("%d/%m/%Y"),
              "date_to": to_date.strftime("%d/%m/%Y"),
              "nights_in_dst_from": 7,
              "nights_in_dst_to": 28,
              "flight_type": "round",
              "one_for_city": 1,
              "max_stopovers": 0,
              "adult_hand_bag": 1,
              "curr": "EUR"}
        response = requests.get(url=location_endpoint, params=query, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to_code}")
            return None
        
        # FlightData
        flightData = FlightData(
            data['price'],
            data['route'][0]['cityFrom'],
            data['route'][0]['flyFrom'],
            data['route'][0]['cityTo'],
            data['route'][0]['flyTo'],
            data['route'][0]['local_departure'].split('T')[0],
            data['route'][1]['local_departure'].split('T')[0]
        )

        #print(f"{flightData.city_from}: €{flightData.price}")
        return flightData
        pass
    pass