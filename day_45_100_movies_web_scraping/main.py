import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")
title_list = [title.getText() for title in titles]
title_list.reverse()

for i in range(len(title_list) - 1):
    title_list[i] += "\n"

with open("movies.txt", "w") as file:
    file.writelines(title_list)
