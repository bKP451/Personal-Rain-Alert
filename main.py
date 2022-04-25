import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
# One time weather endpoint
OWE = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = os.getenv("OPEN_WEATHER_API_KEY")

parameters = {
    "lat": 53.904541,
    "lon": 27.561523,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

data = requests.get(OWE, params=parameters)
data.raise_for_status()
open_weather_response = data.json()
weather_code_list = list()
for hour in range(0, 12):
    weather_code = open_weather_response["hourly"][hour]['weather'][0]['id']
    weather_code_list.append(weather_code)
print(weather_code_list)

# looping through the weather_code_list to check each weather_code
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

rain = None
for code in weather_code_list:
    if code < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Hello there. It would be best to company UMBRELLA!! Good day.☕',
        from_='+12672816709',
        to='+9779845813662'
    )
    print("You need to bag up the umbrella!!. \n Have a Good day.")
    print(message.status)