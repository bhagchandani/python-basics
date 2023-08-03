import requests
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "dd99f5486de185c42f1bd1c2e3b204cc"
account_sid = "#############################"
auth_token = "###########################"

parameters = {
	"lat" : 26.449896,
	"lon" : 74.639915,
	"appid" : API_KEY
}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

if(data["weather"][0]["main"] == "Rain"):
	client = Client(account_sid, auth_token)
	message = client.messages \
	                .create(
	                     body="Bring Umbralla, It is going to be rain.",
	                     from_='+##########',
	                     to='+##########'
	                 )
	print(message.status)


