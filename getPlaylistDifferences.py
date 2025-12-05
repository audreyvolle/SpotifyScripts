# Input of playlist name, find differences of what songs are not added to liked songs from that playlist
# python3 getPlaylistDifferences.py '2025'
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import sys

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

SCOPE = "user-library-modify playlist-read-private playlist-read-collaborative"

def get_spotipy_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
    ))

def main():
    #sp = get_spotipy_client()
    playlistName = sys.argv[1]
    print(playlistName)
         


if __name__ == "__main__":
    main()
