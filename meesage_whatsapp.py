import pywhatkit
from datetime import datetime  

# Replace with your WhatsApp phone number (including country code)
phone_number = "+91 9219083613"

# Replace with the name of the contact you want to send the message to
contact_name = "Chuwii 👻"

# Replace with the message you want to send
message = "Hello from Python!"

# Send the message immediately (current time)
pywhatkit.sendwhatmsg(phone_number, message, datetime.now().hour, datetime.now().minute)