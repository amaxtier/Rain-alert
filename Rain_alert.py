import os

import requests
from twilio.rest import Client

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "53c00d4f24d47f60c6834ce38d45ab44"
MY_LAT = 18.485698
MY_LNG = -69.944474

account_sid = "AC649dd0ebd215a0b463949d1e46691c3a"
auth_token = "ef0c61d71d92f061bbc5c15dd0e6e3fa"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "cnt": 4,
}

weather_response = requests.get(
    url=URL,
    params=parameters
)
weather_response.raise_for_status()
print(weather_response.status_code)
data = weather_response.json()["list"]
print(data)

will_rain = False

for dictionary in data:
    if dictionary["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring your umbrella!",
        from_="+18508208159",
        to="+18297415255",
    )
    print(message.status)