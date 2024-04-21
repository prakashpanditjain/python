from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone'
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'
HEADERS = ({'User-Agent': agent, 'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(url, headers= HEADERS)
soup = BeautifulSoup(webpage.content, 'html.parser')
content = soup.find_all('a', attrs={'class': "title"})
print(content)
product_name =[]
for i in range(len(content)):
    product_name.append(content[i].text.strip().replace('...', ''))
print(product_name)
