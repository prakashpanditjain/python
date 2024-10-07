import os
import requests
import bs4
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('openlib_api')
# print(url)
response = requests.get(url)
# print(response)

if response.status_code == 200:
    data= response.json()
print(data['docs'][1])
# for key,value in data['docs'][1]:
#     print(key,value)
    # for key, value in data.items():
    #     print(key,a)
# htmlparser = bs4.BeautifulSoup(response.text, 'html.parser')
# print(htmlparser)
#
# remark = []
# for e in htmlparser.find_all('p', {"class":"leading-relaxed mb-6 dark:text-gray-300"}):
#     # print(e)
#     remark.append(e.get_text())

# print(remark)