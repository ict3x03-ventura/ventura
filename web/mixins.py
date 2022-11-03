from twilio.rest import Client
import os 
from dotenv import load_dotenv

# class MessageHandler():
#     email = None
#     otp = None

#     load_dotenv()
#     def __init__(self, email, otp) -> None:
#         self.email = email
#         self.otp = otp
load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

verification = client.verify \
                     .v2 \
                     .services('VA31f1e9fe5914024a035421dd7f0d4e15') \
                     .verifications \
                     .create(channel_configuration={
                          'template_id': os.getenv('TWILIO_TEMPLATE_ID'),
                          'from': 'alphonse@gmail.com',
                          'from_name': 'Hotel Ventura Admin'
                      }, to='cloudynineteen95@gmail.com', channel='email')
print(verification.sid)
