import os
import smtplib
import requests
from  dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
source_number = os.environ['TWILIO_PHONE_NUMBER']
destination_number = os.environ['RECIPIENT_PHONE_NUMBER']
my_email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)
        pass

    def send_sms(self,message):
         message = self.client.messages.create(
             body=message,
             from_=source_number,
             to=destination_number
         )
         print(message.status)
         pass
    
    
    
    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in  emails:
                connection.sendmail(from_addr=my_email, 
                                to_addrs=email, 
                                msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))

        pass
    
    pass