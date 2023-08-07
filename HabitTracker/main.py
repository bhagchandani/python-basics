import requests
from datetime import datetime

USERNAME = "beena"
TOKEN = "F6USKBI221MKSBCJ2598GZ3DSSLT2ISK"
GRAPHID = "graphbeena1"

USER_PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
	"token" : TOKEN,
	"username" : USERNAME,
	"agreeTermsOfService" : "yes",
	"notMinor" : "yes"
}

# response = requests.post(url=USER_PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_PIXELA_ENDPOINT = f"{USER_PIXELA_ENDPOINT}/{USERNAME}/graphs"

user_graph_params = {
	"id" : "graphbeena1",
	"name" : "Cycling Graph",
	"unit" : "Km",
	"type" : "float",
	"color" : "ajisai"
}

headers = {
	"X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_PIXELA_ENDPOINT, json=user_graph_params, headers=headers)

# print(response.text)

########## POST A PIXIL #################3
########## POST A PIXIL #################3
GRAPH_PIXEL_ENDPOINT = f"{USER_PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}"
#yesterday Date

todays = datetime.now()
formatted_date = todays.strftime("%Y%m%d")

post_pixel_params = {
	"date" : formatted_date,
	"quantity" : "5.0"
}

# response = requests.post(url=GRAPH_PIXEL_ENDPOINT, json=post_pixel_params, headers=headers)

# print(response.text)

######Update the graph pixel
yesterday_date = datetime(year=2023, month=8, day=6)

formatted_date = yesterday_date.strftime("%Y%m%d")

UPDATE_PIXEL_ENDPOINT = f"{USER_PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}/{formatted_date}"

update_pixel_params = {
	"quantity" : "8.5"
}

# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_params, headers=headers)
# print(response.text)


######DELETE the graph pixel
yesterday_date = datetime(year=2023, month=8, day=6)

formatted_date = yesterday_date.strftime("%Y%m%d")

DELETE_PIXEL_ENDPOINT = f"{USER_PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}/{formatted_date}"


response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
print(response.text)
