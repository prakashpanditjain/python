import requests
from bs4 import BeautifulSoup


response = requests.get('https://news.ycombinator.com/news')
markup_text  = response.text


soup = BeautifulSoup(markup_text, "html.parser")
#
span = soup.find_all(name='span', class_='titleline')

article_text= []
article_link = []
# print(span)
for tag in span:
    tag_a = tag.find(name='a')
    article_text.append(tag_a.text)

    tag_href = tag_a.get('href')
    article_link.append(tag_href)

article_upvotes =[int(points.getText().split(' ')[0]) for points in soup.find_all(name='span', class_='score')]
# print(article_upvotes)

article_index = article_upvotes.index(max(article_upvotes))

print(f"Name of the article: {article_text[article_index]}\nlink:  {article_link[article_index]} \nupvotes:-  {article_upvotes[article_index]}:upvotes")
