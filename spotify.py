import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials


#File for everything related to searching the spotify API



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
        song_names[heize_dict[track["uri"]]] = track

    return song_names


def get_song_features(song_id):
    return spotify.audio_features(song_id)

def get_track(song_id):
    return spotify.track(song_id)