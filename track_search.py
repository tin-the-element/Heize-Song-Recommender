import song_formula

def delete_duplicate(tracks):
    prev_key = ""
    prev_value = ""
    x = 1
    for key, values in list(tracks.items()):
        if prev_key in key and x != 1:
            
            diff = song_formula.define_formula(prev_value) - song_formula.define_formula(values)
            if abs(diff) <= 10:
                tracks.pop(key)
        prev_key = key
        prev_value = values
        x += 1
    return tracks

def find_similar_tracks(tracks, song):
    similar_songs = {}
    closest_songs = []
    old_value = None
    '''
    Use the outside index and tracks_length as boundaries for finding the max five closest songs to the song chosen
    '''
    user_value = song_formula.define_formula(song)
    outside_index = 0
    tracks_length = len(tracks)

    for key, values in (tracks.items()):
        outside_index += 1
        if user_value < current_value:
            inside_index = 0
            other = outside_index
            while inside_index!= 5 or other != 0:
                other -= 1
                inside_index += 1

    #Find a way to index through a dictionary
    return 
