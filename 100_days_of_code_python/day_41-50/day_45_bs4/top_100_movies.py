import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)

text = response.text

soup  = BeautifulSoup(text, "html.parser")

get_h3_tags = soup.find_all(name="h3", class_="title")

Movies_names = [tag.text for tag in get_h3_tags[::-1]]

print(Movies_names)

with open("movies.txt","w") as file:
    for movie in Movies_names:
        file.write(f"{movie}\n")

