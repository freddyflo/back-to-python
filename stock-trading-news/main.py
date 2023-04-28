import requests
import os
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ['STOCK_API_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": COMPANY_NAME,
    "apikey": STOCK_API_KEY,
}
# response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
# response.raise_for_status()
# data = response.json()["Time Series (Daily)"]
# data_list = [value for (key, value) in data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]

#Get the day before yesterday's closing stock price
# day_before_yesterday_data = data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# difference = abs(int(yesterday_closing_price) - int(day_before_yesterday_closing_price))

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# diff_percent = (difference / float(yesterday_closing_price)) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# news_parameters = {
#     "q": COMPANY_NAME,
#     "sources": "bbc-news,the-verge",
#     "domains": "bbc.co.uk,techcrunch.com",
#     "from_param": "",
#     "to": "",
#     "language": "en",
#     "sort_by": "",
#     "page": 2
# }



# if diff_percent > 5:
#     print("Get news")
#     pass
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "language": "en",
}
news_reponse = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_reponse.raise_for_status()
articles = news_reponse.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#Create a new list of the first 3 article's headline and description using list comprehension.
up_down = "🔺"
formatted_articles = [f"{STOCK_NAME}: {up_down}\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]


#TODO 9. - Send each article as a separate message via Twilio. 
# ---------------- TWILIO ---------------- #
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_PHONE_NUMBER']
recipient_number = os.environ['RECIPIENT_PHONE_NUMBER']

client = Client(account_sid, auth_token)
for article in formatted_articles:
    message = client.messages.create(
                                body=article,
                                from_=twilio_number,
                                to=recipient_number
                            )
print(message.status)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

