import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.environ["SHEETY_API_KEY"]
APP_ID = os.environ["SHEETY_APP_ID"]
ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_WORKOUT_ENDPOINT = os.environ["SHEETY_WORKOUT_ENDPOINT"]

today = datetime(year=2023, month=5, day=1)
today_dated_formated = today.strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

HEADERS  = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY, 
}

user_input = input("Tell me what exercise you did: ")

PARAMETERS = {
    "query": user_input
}

response = requests.post(url=ENDPOINT, json=PARAMETERS, headers=HEADERS)
response.raise_for_status()
data = response.json()

exercise = data["exercises"][0]["name"].title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]




SHEETY_PARAMETERS = {
"workout": {
    "date": today_dated_formated,
    "time": now_time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories,
    }
}




sheety_response = requests.post(url=SHEETY_WORKOUT_ENDPOINT, json=SHEETY_PARAMETERS)
sheety_response.raise_for_status()
print(sheety_response.text)