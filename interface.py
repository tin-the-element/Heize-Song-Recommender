import tkinter as tk
import spotify
import prints
import track_search
def onclick(song_scores, artists_songs, enter):
    user_song = enter.get()
    while user_song != "exit":
        
        user_song = spotify.get_song_features(input("Enter a song id, enter exit is you want quit: "))

        related_songs = track_search.find_similar_tracks(song_scores, user_song)

        prints.print_final_songs(related_songs, artists_songs)

def interface(song_scores, artists_songs):
    program = tk.Tk()
    program.title("Heize Song Recommender")
    label_title = tk.Label(program, width = 100)
    label_title["text"] = "Enter Song URL/URI/ID Below!"
    label_title.grid(row = 0, column = 0)
    enter = tk.Entry(program, width = 100, bd= 5)
    enter.grid(row = 1, column = 0)
    button = tk.Button(program, text="enter", height = 5, width = 10, command = onclick(song_scores, artists_songs, enter))
    button.grid(row = 1, column = 1)
    
    program.mainloop()