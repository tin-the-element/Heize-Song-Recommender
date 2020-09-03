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
    similar_songs = []
    closest_songs = {}
    old_value = None
    '''
    Use the outside index and tracks_length as boundaries for finding the max five closest songs to the song chosen
    '''
    user_value = song_formula.define_formula(song[0])
    tracks_length = len(tracks)
    track_values = [features for name, features in sorted(tracks.items(), key=lambda item: item[1])]
    track_names = [name for name, features in sorted(tracks.items(), key=lambda item: item[1])]
    for i in range(tracks_length):
        current_value = track_values[i]
        if user_value < current_value:
            inside_index = 0
            other = i
            current_song = None
            while inside_index != 5 and other != 0:
                current_value = track_values[other]
                current_name = track_names[other]
                other -= 1
                inside_index += 1
                closest_songs[current_name] = abs(current_value - user_value)
            
            inside_index = 0
            other = i + 1
            while inside_index!= 5 and other != tracks_length:
                current_value = track_values[other]
                current_name = track_names[other]
                other += 1
                inside_index += 1
                closest_songs[current_name] = abs(current_value - user_value)
            break
    
    similar_songs = [key for key, value in sorted(closest_songs.items(), key=lambda item: item[1])]
    

    closest_songs = [similar_songs[i] for i in range(5)]
    #Find a way to index through a dictionary
    return closest_songs

    '''
    So I could just do a dict comprehension anytime I do dictionary.values/dictionary.keys/dictionary.items
    '''
