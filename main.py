import search
import song_formula

#The uri of heize (can hypothetically put any artist in here)
heize_uri = 'spotify:artist:5dCvSnVduaFleCnyy98JMo'

artists_songs = search.get_songs(heize_uri)

song_scores = {}

for name, track in artists_songs.items():
    song_scores[name] = song_formula.define_formula(track["danceability"], track["energy"], track["acousticness"], track["tempo"], track["valence"])

sorted_scores = {name: score for name, score in sorted(song_scores.items(), key=lambda item: item[1])}
for name, track in sorted_scores.items():
    print(str(name) + " : " + str(track))