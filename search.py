import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
print()
print('THIS IS A NEW PROGRAM')
print('---------------------')
print()

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
heize_uri = 'spotify:artist:5dCvSnVduaFleCnyy98JMo'

albums = spotify.artist_albums(heize_uri)
albums = albums['items']
heize_albums = [album['id'] for album in albums]
heize_dict = {}
for album in heize_albums:
    tracks = spotify.album_tracks(album)
    #pretty_print = json.dumps(tracks, indent=2)
    #print(pretty_print)

    for track in tracks['items']:
        heize_dict[track["uri"]] = track["name"]

print(heize_dict)
results = spotify.audio_features(heize_dict.keys())
for track in results:
    pretty_print = json.dumps(track, indent=2)
    print("\n" + heize_dict[track["uri"]] + "\n")
    print(pretty_print)