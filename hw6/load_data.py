"""
CMSC 14100
Updated Autumn 2025

Data Loading Functions for Homework #6
"""

import csv

def load_albums():
    """
    Load abbreviation-to-album mappings from the Corpus of Taylor Swift

    Inputs:
       None

    Output (list of lists of str): A list of lists in which each inner list 
                                   contains two strings, which respectively 
                                   represent an album abbreviation and the 
                                   corresponding album name.
    """
    with open("data/albums.tsv") as albums:
        return [row for row in csv.reader(albums, delimiter='\t')]

def load_songs(num_lines = -1):
    """
    Load album-to-song mappings from the Corpus of Taylor Swift

    Input:
        num_lines (int): An optional parameter that, if greater than 0, 
                         returns the first num_lines of album-to-song mappings
                         to aid in debugging

    Output (list of lists of str): A list of lists in which each inner list 
                                   contains three strings representing the 
                                   album abbreviation, the track number, and 
                                   the song title, respectively.
    """
    with open("data/cots-song-details.tsv") as songs:
        output = [row for row in csv.reader(songs, delimiter='\t',
                                            quoting=csv.QUOTE_NONE)]
        # remove header
        del output[0]
    if num_lines == -1:
        return output
    else:
        return output[:num_lines]


def load_lyrics(num_lines = -1):
    """
    Load song lyrics from the Corpus of Taylor Swift

    Input:
        num_lines (int): An optional parameter that, if greater than 0, 
                         returns the first num_lines of album-to-song mappings
                         to aid in debugging

    Output (list of lists of str): A list of lists in which each inner list 
                                   contains two strings representing the 
                                   timing (including album and song) and  
                                   the lyric at that time, respectively.
    """
    with open("data/cots-lyric-details.tsv") as lyrics:
        output = [row for row in csv.reader(lyrics, delimiter='\t', 
                                            quoting=csv.QUOTE_NONE)]
    if num_lines == -1:
        return output
    else:
        return output[:num_lines]
