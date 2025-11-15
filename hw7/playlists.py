import csv
from hw7 import Duration, Song, Playlist

def get_playlists():
    playlists = {}
    counter = 0
    with open("playlists.csv") as f:
        for playlist, artist, title, length in csv.reader(f):
            m, s = length.split(":")
            if playlist not in playlists:
                playlists[playlist] = []
            playlists[playlist].append(Song(title, artist, Duration(int(m), int(s)),
                                       counter % (6 - len(playlists)) == 0))
            counter += 1
    rv = []
    for playlist in sorted(playlists.keys()):
        rv.append(Playlist(playlist, playlists[playlist]))
    return rv
