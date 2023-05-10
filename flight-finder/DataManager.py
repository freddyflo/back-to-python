import requests
import os
from  dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
sheety = os.environ["SHEETY_USER_ENDPOINT"]

class DataManager:

    def __init__(self):
        self.destination_data = {}
        pass

    def get_destination_information(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        sheet_data = response.json()
        self.destination_data = sheet_data["prices"]
        return self.destination_data
        pass

    def update_destination_codes(self):
        for city in self.destination_data:
            query = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=query
            )
            print(response.text)
        pass

    def get_customer_emails(self):
        response = requests.get(url=sheety)
        response.raise_for_status()
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
        pass
    pass