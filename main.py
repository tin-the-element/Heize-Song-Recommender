import spotify
import song_formula
import prints
import track_search
import interface
from collections import OrderedDict

print("\nHeize Song Recommender\n----------\n")
#The uri of heize (can hypothetically put any artist in here)
heize_uri = 'spotify:artist:5dCvSnVduaFleCnyy98JMo'
#heize_uri = 'spotify:artist:3qNVuliS40BLgXGxhdBdqu'
#Get the artists song from the uri
artists_songs = spotify.get_songs(heize_uri)

artists_songs = {name: features for name, features in sorted(artists_songs.items(), key=lambda item: item[0])}
#Delete duplicates
artists_songs = track_search.delete_duplicate(artists_songs)

#Use the dictionary of audio features to create scores
song_scores = OrderedDict()

for name, track in artists_songs.items():
    song_scores[name] = song_formula.define_formula(track)
        

#Sorting the albums by score
sorted_scores = {name: score for name, score in sorted(song_scores.items(), key=lambda item: item[1])}

#Options to print to help me code
#prints.options(artists_songs, sorted_scores)

#Enter song_id

interface.interface(song_scores, artists_songs)


#TO-DO
#  - Delete Duplicate Songs
#  - Separate Instrumental Songs (If statement?)
#  - Find a formula