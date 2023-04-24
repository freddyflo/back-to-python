import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 48.856613 # Your latitude
MY_LONG = 2.352222 # Your longitude
EMAIL = ""
PASSWORD = ""

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    LATITUDE_ERROR_MARGIN_POSITIVE = MY_LAT + 5
    LATITUDE_ERROR_MARGIN_NEGATIVE = MY_LAT - 5
    LONGITUDE_ERROR_MARGIN_POSITIVE = MY_LONG + 5
    LONGITUDE_ERROR_MARGIN_NEGATIVE = MY_LONG - 5

    if LATITUDE_ERROR_MARGIN_NEGATIVE <= iss_latitude <= LATITUDE_ERROR_MARGIN_POSITIVE and \
        LONGITUDE_ERROR_MARGIN_NEGATIVE <= iss_longitude <= LONGITUDE_ERROR_MARGIN_POSITIVE: \
        return True
    pass

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True



SMTP_PORT = 587
SMTP_GMAIL_SERVER = "smtp.gmail.com"
if is_iss_overhead() and is_night():
    connection = smtplib.SMTP(SMTP_GMAIL_SERVER, SMTP_PORT)
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.send_message(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg="Subject: Look Up👆\n\n The ISS is above you in the sky"
    )
    pass



