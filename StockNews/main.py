import requests
from datetime import datetime 
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "##########################"
NEWS_API_KEY = "##########################"
account_sid = "##########################"
auth_token = "##########################"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol"   : STOCK_NAME,
    "apikey"   : STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = (difference/float(yesterday_closing_price)) * 100


#percentage is greater than 5 then print("Get News").
if diff_percentage > 1:
    news_params = {
        "apiKey"   : NEWS_API_KEY,
        "q" :  COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
  
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    initial_article = news_data[:3]
    
    #Create a new list of the first 3 article's headline and description using list comprehension.

    newMessage = [f"Headline: {article['title']} \n Brief: {article['description']}" for article in initial_article]
  

    #TODO 9. - Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body=newMessage,
                         from_='+#############',
                         to='+#############'
                     )
    print(message.status)
   