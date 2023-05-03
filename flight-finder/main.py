import requests
from pprint import pprint
from datetime import datetime, timedelta
import os
from  dotenv import load_dotenv
from twilio.rest import Client
from NotificationManager import NotificationManager
from FlightSearch import FlightSearch
from DataManager import DataManager


load_dotenv()

flightSearch = FlightSearch()
dataManager = DataManager()
notificationManager = NotificationManager()

# -------- SHEETY -------- #
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

# -------- TEQUILA -------- #
TEQUILA_ENDPOINT = os.environ["TEQUILA_ENDPOINT"]
TEQUILA_AP_KEY = os.environ["TEQUILA_AP_KEY"]



# -------- TWILIO SMS ------ #
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
source_number = os.environ['TWILIO_PHONE_NUMBER']
destination_number = os.environ['RECIPIENT_PHONE_NUMBER']


start_date = datetime.now() + timedelta(days=1)
six_month_from_date = datetime.now() + timedelta(days=(6 * 30))




sheet_data = dataManager.get_destination_information()

CITY_OF_ORIGIN = "PAR"

if sheet_data[0]["iataCode"] == "":
    for data in sheet_data:
        data["iataCode"] = flightSearch.get_destination_code(data["city"])
    dataManager.destination_data = sheet_data
    dataManager.update_destination_codes()

for destination in sheet_data:
    flight = flightSearch.find_flight(
        CITY_OF_ORIGIN,
        destination["iataCode"],
        from_date=start_date,
        to_date=six_month_from_date
    )
    
    if flight is not None and flight.price < destination["lowestPrice"]:
        notificationManager.send_sms(
            message=f"Low price alert! Only €{flight.price} to fly from {flight.city_from}-{flight.fly_from} to {flight.city_to}-{flight.fly_to}, from {flight.out_date} to {flight.return_date}.")
   

