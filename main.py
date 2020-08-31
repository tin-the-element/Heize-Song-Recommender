import search
import song_formula
import prints

print("\nNew Program\n----------\n")
#The uri of heize (can hypothetically put any artist in here)
heize_uri = 'spotify:artist:5dCvSnVduaFleCnyy98JMo'

#Get the artists song from the uri
artists_songs = search.get_songs(heize_uri)


#Use the dictionary of audio features to create scores
song_scores = {}

for name, track in artists_songs.items():
    song_scores[name] = song_formula.define_formula(track["danceability"], track["energy"], track["acousticness"], track["tempo"], track["valence"], track["instrumentalness"])

#Sorting the albums by score
sorted_scores = {name: score for name, score in sorted(song_scores.items(), key=lambda item: item[1])}

#Options to print to help me code
prints.options(artists_songs, sorted_scores)



#search.print_songs(artists_songs)

#TO-DO
#  - Delete Duplicate Songs
#  - Separate Instrumental Songs (If statement?)
#  - Find a formula