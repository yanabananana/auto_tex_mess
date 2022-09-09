#Creating auto-mated text messaages with Python

#Collection of preset messages

Good_Morning_Quotes = [
    'Morning K',
    'Morning Babe',
    'Morning, how did u sleep?',

]
#Twilio REST API - send preset message using API 

from twilio.rest import Client
import schedule 
def send_message(quote):
    account ="ACfe282a3392a13c9ba7fc4effc06ca4f2"
    token = " "
    client = Client (account.token)

    client.messages.create(to = cellphone, from = twilio_number, body = quote)

# send a message in the morning
schedule.every().day.at("10:00".do(send_message,Good_Morning_Quotes[3])