from bs4 import BeautifulSoup
import requests
import pandas
import json

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

movies_data = response.text

soup = BeautifulSoup(movies_data, 'html.parser')
script = soup.find("script", type="application/json")
data = json.loads(script.string)

all_titles = []

for film in data["props"]["pageProps"]["data"]["getArticleByFurl"]["_layout"][3]["content"]["images"]:
    all_titles.append((film["titleText"]))

all_titles = all_titles[::-1]

with open("movies.txt", "w") as data_file:
	for movie in all_titles:
		data_file.write(f"{movie}\n")



