from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
h_tags = soup.find_all("h3")
movie_titles = [h_tag.getText() for h_tag in h_tags]
movies = movie_titles[::-1]

with open("output.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")


