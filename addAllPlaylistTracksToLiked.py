import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

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

def get_all_playlist_tracks(sp, playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)

    while results:
        tracks.extend(results["items"])
        if results["next"]:
            results = sp.next(results)
        else:
            results = None

    track_ids = [
        item["track"]["id"]
        for item in tracks
        if item["track"] and item["track"]["id"]
    ]
    return track_ids

def main():
    sp = get_spotipy_client()

    print("Fetching playlists...")
    playlists = sp.current_user_playlists()

    all_track_ids = []

    while playlists:
        for pl in playlists["items"]:
            print(f"→ Reading playlist: {pl['name']}")

            track_ids = get_all_playlist_tracks(sp, pl["id"])
            print(f"  Found {len(track_ids)} tracks")

            all_track_ids.extend(track_ids)

        if playlists["next"]:
            playlists = sp.next(playlists)
        else:
            playlists = None

    print(f"\nTotal tracks found: {len(all_track_ids)}")
    all_track_ids = list(set(all_track_ids))
    print(f"Unique tracks: {len(all_track_ids)}")

    print("\nAdding tracks to Liked Songs...")

    # batch in groups of 50
    for i in range(0, len(all_track_ids), 50):
        batch = all_track_ids[i:i+50]
        sp.current_user_saved_tracks_add(batch)
        print(f"Added {i + len(batch)} of {len(all_track_ids)}")

if __name__ == "__main__":
    main()
