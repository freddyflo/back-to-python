from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv

load_dotenv()


CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']


sp = spotipy.Spotify(
                    auth_manager=SpotifyOAuth(
                        client_id=CLIENT_ID, 
                        client_secret=CLIENT_SECRET,
                        scope="playlist-modify-private",
                        redirect_uri="http://localhost:8888/callback",
                        show_dialog=True,
                        cache_path="token.txt"
                        )
                    )

user_id = sp.current_user()["id"]


ans = input("Which year do you to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{ans}")
response.raise_for_status()

billboard_chart = response.text

soup = BeautifulSoup(billboard_chart, "html.parser")

song_spans = soup.select("li ul li h3")


song_titles = [ song_title.getText().strip() for song_title in song_spans]


song_uris = []
year = ans.split("-")[0]
if year == "":
    year = "2023"

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

# Create user playlist
user_playlist = sp.user_playlist_create(
                    user=user_id,
                    name=f"{year} Billboard 100",
                    public=False,
                    collaborative=False,
                    description="100 Billboard tracks")


sp.playlist_add_items(playlist_id=user_playlist["id"], items=song_uris)