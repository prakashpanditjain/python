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