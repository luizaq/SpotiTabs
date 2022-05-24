import requests
import sys
#import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials
#https://spotipy.readthedocs.io/en/2.12.0/


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'



def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    json_resp = response.json()

    if 'error' in json_resp:
        print("O token de autorização do Spotify expirou, encerrando...")
        sys.exit()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link
    }

    return current_track_info

