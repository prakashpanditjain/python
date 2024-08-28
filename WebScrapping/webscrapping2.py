import os

import requests
import bs4
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('code_with_harry')
# print(url)
response = requests.get(url)

htmlparser = bs4.BeautifulSoup(response.text, 'html.parser')
# print(htmlparser)

remark = []
for e in htmlparser.find_all('p', {"class":"leading-relaxed mb-6 dark:text-gray-300"}):
    # print(e)
    remark.append(e.get_text())

print(remark)