import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


SCOPE = "user-read-recently-played"

def get_spotipy_client():
    load_dotenv()
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id= os.getenv('CLIENT_ID'),
        client_secret= os.getenv('CLIENT_SECRET'),
        redirect_uri= os.getenv('REDIRECT_URI'),
        scope=SCOPE,
    ))

def main():
    sp = get_spotipy_client()

    results = sp.current_user_recently_played(limit=20)

    print("\nRecently Played Tracks:")
    for item in results["items"]:
        track = item["track"]
        print(f"- {track['name']} — {track['artists'][0]['name']}")


if __name__ == "__main__":
    main()
