from bs4 import BeautifulSoup
import requests

from dotenv import load_dotenv
import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

date = input("which year you would like to travel to in YYYY-MM-DD format: ")
year = date[0:4]
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

music_tags = soup.select(selector="ul li .c-title")
music_titles = [tag.getText().strip() for tag in music_tags]

scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope=scope,
        show_dialog=True,
        cache_path="token.txt"
    ))

user_id = sp.current_user()["id"]

music_urls = []
for music in music_titles:
    result = sp.search(q=f"track:{music} year:{year}", type="track")
    try:
        url = result['tracks']['items'][0]["uri"]
        music_urls.append(url)
    except IndexError:
        print(f"{music} doesn't exist in Spotify. Skipped")

play_list = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)


sp.playlist_add_items(playlist_id=play_list["id"], items=music_urls)
# print(play_list)



