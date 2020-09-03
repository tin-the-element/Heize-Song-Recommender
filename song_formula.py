#Specific Keys Needed
#Danceability, Energy, Acousticness, Tempo, Valence
'''
Danceability - rate of how danceable it is - Distribution is fairly normal with more leaning to more danceable
Energy - Measure of intensitivity and activity ie. Death Metal has high energy Bach has low energy - similar distribution with danceability
Tempo - Pace of the song (How fast it is), also really balanced in the middle
Valence - Describes the cheerfulness of the song, distribution is really even actually
'''
def define_formula(track): 
    danceability = track["danceability"]
    energy = track["energy"]
    tempo = track["tempo"]
    valence = track["valence"]
    instrumentalness = track["instrumentalness"]

  
    song_score = 0
    #danceability + energy + acousticness + tempo + valence + 

    if instrumentalness > .04:
        song_score += 5000

    #Tempo
    song_score += tempo / 10

    #Valence
    song_score += valence * 300
    
    #Danceability
    song_score += danceability * 300

    #Energy
    song_score += energy * 300

    return song_score


