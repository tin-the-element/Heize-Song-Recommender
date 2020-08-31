import json

def print_songs(tracks, option):
    for name, track in tracks.items():
        print("\n" + name + "\n")
        print(track[option])

def write_to_file(tracks):
    f = open("songs.txt", "a")
    for name, track in tracks.items():
        pretty_print = json.dumps(track, indent=2)
        f.write("\n" + name + "\n")
        f.write(pretty_print)

def print_specific_song(tracks, song):
    print("\n" + song + "\n")
    print(tracks[song])

def print_scores(sorted_scores):
    for name, track in sorted_scores.items():
        print(str(name) + " : " + str(track))

def options(tracks, scores):
    option = int(input("Input 1 for print_songs \nInput 2 for print_specific_song \nInput 3 for print_scores \n"))

    if option == 1:
        key = input("Enter a certain object ")
        print_songs(tracks, key)
    elif option == 2:
        key = input("Enter a specific song ")
        print_specific_song(tracks, key)
    elif option == 3:
        print_scores(scores)
    elif option == 4:
        write_to_file(tracks)
    