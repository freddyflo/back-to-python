import os
from  dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
source_number = os.environ['TWILIO_PHONE_NUMBER']
destination_number = os.environ['RECIPIENT_PHONE_NUMBER']

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
    
    pass