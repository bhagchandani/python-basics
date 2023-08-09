from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_texts = []
article_links = []
article_score = []

article_text = soup.find_all(name="span", class_="titleline")
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

for ar_tag in article_text:
	article_texts.append(ar_tag.find("a").get_text())
	article_links.append(ar_tag.find("a").get("href"))


laragest_number = max(article_upvotes)
laraged_number_index = article_upvotes.index(laragest_number)


print(article_texts[laraged_number_index+1])
print(article_links[laraged_number_index+1])