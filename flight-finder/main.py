import requests
from pprint import pprint
import datetime 
import os
from  dotenv import load_dotenv
from twilio.rest import Client
from NotificationManager import NotificationManager

load_dotenv()


# -------- SHEETY -------- #
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

# -------- TEQUILA -------- #
TEQUILA_ENDPOINT = os.environ["TEQUILA_ENDPOINT"]
TEQUILA_AP_KEY = os.environ["TEQUILA_AP_KEY"]

response = requests.get(url=SHEETY_ENDPOINT)
response.raise_for_status()
sheet_data = response.json()


# -------- TWILIO SMS ------ #
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
source_number = os.environ['TWILIO_PHONE_NUMBER']
destination_number = os.environ['RECIPIENT_PHONE_NUMBER']
notificationManager = NotificationManager()


def get_destination_code(city_name):
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    headers = {"apiKey": TEQUILA_AP_KEY}
    query =  {"term": city_name, "location_types": "city"}
    response = requests.get(url=location_endpoint, headers=headers, params=query)
    results = response.json()["locations"]
    code = results[0]["code"]
    print(f"Code: {code}")
    return code

start_date = datetime.date.today() + datetime.timedelta(days=1)
end_date = start_date + datetime.timedelta(days=180)




def find_cheap_flight(code):
    location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
    headers = {"apiKey": TEQUILA_AP_KEY}
    query =  {"fly_from": "PAR", 
              "fly_to": code, 
              "date_from": start_date.strftime("%d/%m/%Y"),
              "date_to": end_date.strftime("%d/%m/%Y"),
              "nights_in_dst_from": 7,
              "nights_in_dst_to": 28,
              "flight_type": "round",
              "one_for_city": 1,
              "max_stopovers": 0,
              "adult_hand_bag": 1,
              "curr": "EUR"}
    response = requests.get(url=location_endpoint, params=query, headers=headers)
    response.raise_for_status()
    return response.json()["data"][0]
    pass


for element in sheet_data['prices']:
    code = element["iataCode"]
    lowest_price = element["lowestPrice"]
    results = find_cheap_flight(code)
    print(f"#--------------{code}------------#")
    # print(f"Price: €{results['price']}")
    # print(f"Price: {results['deep_link']}")
    # print(f"Orign City: {results['route'][0]['cityFrom']}")
    # print(f"Orign Airport: {results['route'][0]['flyFrom']}")
    # print(f"Destination City: {results['route'][0]['cityTo']}")
    # print(f"Destination Airport: {results['route'][0]['flyTo']}")
    # print(f"Out Date: {results['route'][0]['local_departure'].split('T')[0]}")
    # print(f"Return Date: {results['route'][1]['local_departure'].split('T')[0]}")
    if results['price'] < int(lowest_price):
        print("Low price alert")
        body_message = {
            f"\nLow price alert\n***********\n \
                                Only €{results['price']} to fly from  \
                                {results['route'][0]['cityFrom']}-{results['route'][0]['flyFrom']} \
                                {results['route'][0]['cityTo']}-{results['route'][0]['flyTo']} \
                                from {results['route'][0]['local_departure'].split('T')[0]} to \
                                {results['route'][1]['local_departure'].split('T')[0]} \
                                {results['deep_link']}"
        }
        notificationManager.send_sms(message=body_message)
        # message = client.messages.create(
        #                         body=f"\nLow price alert\n***********\n \
        #                         Only €{results['price']} to fly from  \
        #                         {results['route'][0]['cityFrom']}-{results['route'][0]['flyFrom']} \
        #                         {results['route'][0]['cityTo']}-{results['route'][0]['flyTo']} \
        #                         from {results['route'][0]['local_departure'].split('T')[0]} to \
        #                         {results['route'][1]['local_departure'].split('T')[0]} \
        #                         {results['deep_link']}",
        #                         from_=source_number,
        #                         to=destination_number
        #                     )
        # print(message.status)
    print(f"#-------------- END ------------#")


# for element in sheet_data['prices']:
#     if element["iataCode"] == "TESTING":
#         # update the iataCode column with TESITING
       
#         id = element["id"]
#         SHEETY_UPDATE_ENDPOINT = f"https://api.sheety.co/7274b06db321425f981053ab5a18f989/flightDeals/prices/{id}"
#         parameters = {
#           "price": {
#               "iataCode": get_destination_code(element["city"])
#           }  
#         }
#         response_put = requests.put(url=SHEETY_UPDATE_ENDPOINT, json=parameters)
#         response_put.raise_for_status()
#         pass





