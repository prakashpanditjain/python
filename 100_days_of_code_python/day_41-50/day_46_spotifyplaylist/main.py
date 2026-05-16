from datetime import datetime
import os

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

spotify_secret = os.environ.get("SPOTIFY_SECRET")
spotify_client_id = os.environ.get("SPOTIFY_CLIENT_ID")
redirect_uri = os.environ.get("redirect_uri")
todays_date = datetime.today().date()

# input_date = input("What date would you like to travel to in YYYY-MM-DD format?\n")
url = ""
try:
    # url = "https://www.billboard.com/charts/hot-100/" + f"{input_date}"
    url = "https://www.billboard.com/charts/hot-100/" + f"{todays_date}"
except Exception as e:
    print(f"Please enter the correct date, {e}")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
respose = requests.get(url, headers=header)

#Scrape the Billboard 100 to get the list of songs
soup = BeautifulSoup(respose.text, "html.parser")

#Get the list of top 25 songs from the Billboard 100
all_tags = soup.select("li ul li h3")
song_names = [tag.getText().strip() for tag in all_tags[0:25]] # Get the top 25 songs
print(song_names)

# 2. Create a new playlist
# 3. 0Auth for Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri=redirect_uri,
    client_id=spotify_client_id,
    client_secret=spotify_secret,
    show_dialog=True,
    cache_path="token.txt",
    username="prakashjain",
    )
)
user_id = sp.current_user()["id"] # Get the user id


#  Using the Spotipy documentation, getting list of Spotify song URIs for the
#  list of song names you found from step 1 (scraping billboard 100).
song_uris = []
year = f"{todays_date.year}"
for song in song_names:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)

    except:
        #Add each of the songs into playlist
        print(f"{song} doesn't exist in Spotify. Skipped.")

if len(song_uris) > 5:
    #create a playlist on spofity
    create_playlist = sp.user_playlist_create(user=user_id,
                                              name=f"Today's ({datetime.today()} playlist)",
                                              public=False,
                                              collaborative=False,
                                              description="Playlist for 2025-03-01 Billboard 100")
    playlist_id = create_playlist["id"]

    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

    print("Playlist created successfully")

    #delete the erlier playlist
    