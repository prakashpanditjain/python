from datetime import datetime
from datetime import timedelta

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
url = "https://www.alphavantage.co/query"
parameters = {
    "apikey": "abcdefjasldhfasdfasdf",
    "function": "TIME_SERIES_DAILY",
    # "interval": "5min",
    "symbol": STOCK,
}
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=url, params=parameters)
json = response.json()

today = datetime.today().date()
closing_price = [279.94, 272.35]
for i in range(1, 3):
    dateprice = today - timedelta(days=i)
    # closing_price.append(json['Time Series (Daily)'][str(dateprice)]['4. close'])

with open("./closing_price.txt", 'w') as file:
    file.write(f"closing_price = {closing_price}")

closing_price.sort()


# print(closing_price)
def check_per_change(price: list):
    percent_change = round((price[1] - price[0]) / price[1] * 100, 2)
    return percent_change


per_change = check_per_change(closing_price)
NEED_OF_NEWS = False
if per_change > 5:
    NEED_OF_NEWS = True

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
while NEED_OF_NEWS:
    api_key = ""
    url = "https://newsapi.org/v2/top-headlines"
    parameters = {
        "apiKey": "asdkfhjasdp2384273y472bfiwb9832y74",
        "sortBy": "publishedAt",
        "from": today,
        "q": "tesla"
    }

    response = requests.get(url=url, params=parameters)
    content = response.json()
    for i in range(3):
        author = content['articles'][0]['author']
        title = content['articles'][0]['title']
        description = content['articles'][0]['description']
        news = f"author: {author}\nTitle:{title}\nDescription: {description}"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# by connecting it to twilio API we can ssend msg to mobile number using their template
