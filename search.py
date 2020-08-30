import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials



spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))




def get_songs(artist_id):

    #Gets the albums from an artist
    albums = spotify.artist_albums(artist_id)
    albums = albums['items']

    #Gets all the songs from each albums
    heize_albums = [album['id'] for album in albums]
    heize_dict = {}
    for album in heize_albums:
        tracks = spotify.album_tracks(album)

        for track in tracks['items']:
            heize_dict[track["uri"]] = track["name"]

    #Creates a dict of all the different audio features of each song
    song_names = {}
    results = spotify.audio_features(heize_dict.keys())
    for track in results:
        '''
        pretty_print = json.dumps(track, indent=2)
        print("\n" + heize_dict[track["uri"]] + "\n")
        print(pretty_print)
        '''
        song_names[heize_dict[track["uri"]]] = track

    return song_names