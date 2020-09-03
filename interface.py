import tkinter as tk
import spotify
import prints
import track_search
import webbrowser
def callback(url):
    webbrowser.open_new(url)

def button_hover(label):
    label["bg"] = "pink" 

def button_unhover(label):
    label["bg"] = "white" 
   
def onclick(song_scores, artists_songs, enter, program):
    try:
        user_song = enter.get()
        song_name = '"' + spotify.get_track(user_song)["name"] + '"'
        song_artist = '"' + spotify.get_track(user_song)["artists"][0]["name"] + '"'
        user_song = spotify.get_song_features(user_song)

        title = tk.Label(program, width = 100)
        title["text"] = "The Heize songs most similar to " + song_name + " by " + song_artist + ' are '
        title.grid(row = 2, column = 0)
        related_songs = track_search.find_similar_tracks(song_scores, user_song)

        results = prints.print_final_songs(related_songs, artists_songs)

        if len(results) > 0:
            label = tk.Label(program, width = 100, cursor="hand2")
            label["text"] = results[0]
            label.bind("<Button-1>", lambda e: callback(results[1]))
            label.bind("<Enter>", lambda e: button_hover(label))
            label.bind("<Leave>", lambda e: button_unhover(label))
            label.grid(row = 4, column = 0)
        if len(results) > 2:
            label1 = tk.Label(program, width = 100, cursor="hand2")
            label1["text"] = results[2]
            label1.bind("<Button-1>", lambda e: callback(results[3]))
            label1.bind("<Enter>", lambda e: button_hover(label1))
            label1.bind("<Leave>", lambda e: button_unhover(label1))
            label1.grid(row = 5, column = 0)
        if len(results) > 4:    
            label2 = tk.Label(program, width = 100, cursor="hand2")
            label2["text"] = results[4]
            label2.bind("<Button-1>", lambda e: callback(results[5]))
            label2.bind("<Enter>", lambda e: button_hover(label2))
            label2.bind("<Leave>", lambda e: button_unhover(label2))
            label2.grid(row = 6, column = 0)
        if len(results) > 6:
            label3 = tk.Label(program, width = 100, cursor="hand2")
            label3["text"] = results[6]
            label3.bind("<Button-1>", lambda e: callback(results[7]))
            label3.bind("<Enter>", lambda e: button_hover(label3))
            label3.bind("<Leave>", lambda e: button_unhover(label3))
            label3.grid(row = 7, column = 0)
        if len(results) > 8:
            label4 = tk.Label(program, width = 100, cursor="hand2")
            label4["text"] = results[8]
            label4.bind("<Button-1>", lambda e: callback(results[9]))
            label4.bind("<Enter>", lambda e: button_hover(label4))
            label4.bind("<Leave>", lambda e: button_unhover(label4))
            label4.grid(row = 8, column = 0)
    except:
        label = tk.Label(program, width = 100)
        label["text"] = "Please enter a spotify song URL/URI/ID"
        label.grid(row = 4, column = 0)
        
        label1 = tk.Label(program, width = 100)
        label1["text"] = ""
        label1.grid(row = 5, column = 0)

        label2 = tk.Label(program, width = 100)
        label2["text"] = ""
        label2.grid(row = 6, column = 0)

        label3 = tk.Label(program, width = 100)
        label3["text"] = ""
        label3.grid(row = 7, column = 0)

        label4 = tk.Label(program, width = 100)
        label4["text"] = ""
        label4.grid(row = 8, column = 0)

    
    

def interface(song_scores, artists_songs):
    program = tk.Tk()
    program.title("Heize Song Recommender")
    label_title = tk.Label(program, width = 100)
    label_title["text"] = "Enter Song URL/URI/ID Below!"
    label_title.grid(row = 0, column = 0)
    enter = tk.Entry(program, width = 100, bd= 5)
    enter.grid(row = 1, column = 0)
    button = tk.Button(program, text="enter", height = 5, width = 10, command = lambda: onclick(song_scores, artists_songs, enter, program))
    button.bind("<Enter>", lambda e: button_hover(button))
    button.bind("<Leave>", lambda e: button_unhover(button))
    button.grid(row = 1, column = 1)
    
    program.mainloop()