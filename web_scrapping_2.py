import requests
import pandas
from bs4 import BeautifulSoup

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo'

response= (requests.get(url)).json()
# print(response)
last_refreshed = (response['Meta Data']['3. Last Refreshed'])
price = response['Time Series (5min)'][last_refreshed]['1. open']
symbol = response['Meta Data']['2. Symbol']
print(f' Stock price of {symbol} : {price}')
# last_refreshed =
# print(last_refreshed)



######working with json data
import json

API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
api_endpoint = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

requests1  = requests.get(api_endpoint)
# print(requests1.json())
article = requests1.json().get('articles')
print(article)

for index, article in enumerate(article,start=1):
    print(f'Article {index}: \n {json.dumps(article,sort_keys=True, indent=4)}\n')


# agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'
# HEADERS = ({'User-Agent': agent, 'Accept-Language': 'en-US, en;q=0.5'})
# webpage = requests.get(api_endpoint, headers=HEADERS)
# soup = BeautifulSoup(webpage.content, 'html.parser')
# print(soup)
# print(soup.find('articles'))


response = requests.get('http://api.open-notify.org/astros.json')
people = response.json().get('people')
print(json.dumps(people,sort_keys=True,indent=8))

