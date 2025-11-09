"""
CMSC 14100
Autumn 2025
Homework #6

We will be using anonymous grading, so please do NOT include your name
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import random
import string
from load_data import load_albums, load_songs, load_lyrics


# Exercise 1
def abbrv_to_albums(abbrv_albums):
    """
    Given a list of lists, each of which contains two strings (respectively 
    representing an abbreviation and a full album name), return this data as 
    a dictionary in which the keys are the abbreviations and the values are 
    the full album names.

    Input:
        abbrv_albums (list[list[str]]): A list of lists, each containing an
                                        abbreviation (str) and album name (str)

    Output (dict[str,str]): A dictionary mapping abbreviations (keys) to 
                            full album names (values)
    """
    ### YOUR CODE HERE


# Exercise 2
def song_mapping(songs):
    """
    Given a list of lists, each of which contains three strings (respectively 
    representing an album abbreviation, track number, and song name), return 
    this data as a dictionary of dictionaries in which the outer dictionary 
    maps album abbreviations to inner dictionaries, each of which maps track 
    numbers to song titles.

    Input:
        songs (list[list[str]]]): A list of lists, each containing an album 
                                  abbreviation (str), track number (str), and 
                                  song name (str)

    Output (dict[dict[str,str]]): A dictionary of dictionaries mapping album
                                  abbreviations (str) to inner dictionaries, 
                                  each of which maps track numbers (keys, str) 
                                  to song titles (values, str)
    """
    ### YOUR CODE HERE


# Exercise 3
def most_songs(albums, mapping):
    """
    Given a dictionary of albums (like one created in Exercise 2) and a 
    dictionary of abbreviation-to-album-title mappings (like one created in 
    Exercise 1), return the full name (NOT the abbreviation) of the album 
    with the most songs. If multiple albums contain the same (largest) number 
    of songs, return only the album whose name comes first lexicographically.

    Input:
        albums (dict[dict[str,str]]): A dictionary of dictionaries mapping 
                                      album abbreviations to inner 
                                      dictionaries, each of which maps track 
                                      numbers (str) to song titles (str)
        mapping (dict[str,str]): A dictionary mapping album abbreviations (str)
                                 to full album titles (str)

    Output (str): The full name of the album with the most songs
    """
    ### YOUR CODE HERE

# Exercise 4
def longest_song_title(albums, mapping):
    """
    Given a dictionary of albums (like one created in Exercise 2) and a 
    dictionary of abbreviation-to-album-title mappings (like one created in 
    Exercise 1), return a dictionary whose keys are the full album names 
    (NOT abbreviations) and whose respective values are the title of the 
    song with the longest title on that album. If multiple song titles have the
    same length, return only the song title that comes first lexicographically.

    Input:
        albums (dict[dict[str,str]]): A dictionary of dictionaries mapping 
                                      album abbreviations to inner 
                                      dictionaries, each of which maps track 
                                      numbers (str) to song titles (str)
        mapping (dict[str,str]): A dictionary mapping album abbreviations (str)
                                 to full album titles (str)

    Output (dict[str,str]): A mapping from full album names to the longest 
                            song title on that album
    """
    ### YOUR CODE HERE


# Exercise 5
def word_counts(lyrics):
    """
    Given a list of lists of song lyrics (of the form read in by the 
    load_lyrics() function), return a dictionary mapping words (keys) to 
    counts of the number of times that word appears in the lyrics (values).
    Before computing the counts, remove all capitalization and all punctuation 
    (other than apostrophes). Treat spaces as the only word boundaries. 

    Input:
        lyrics (list[list[str]]): A list of lists of song lyrics of the form 
                                  read in by load_lyrics(). Specifically, the 
                                  second value in each inner list is a line of 
                                  song lyrics (str), while the first value is 
                                  the location in a song (str) and can be 
                                  ignored for this assignment

    Output (dict[str,int]): A mapping from words (case-insensitive, punctuation
                            removed) to counts of how many times that word 
                            appeared in the lyrics
    """
    ### YOUR CODE HERE


# Exercise 6
def frequent_words(counts, threshold):
    """
    Given a dictionary of word counts in lyrics (like the one returned by 
    Exercise 5), return a list of words that appeared at least a threshold 
    number of times in those lyrics. The list returned must be sorted 
    lexicographically.

    Input:
        counts (dict[str,int]): A dictionary mapping words (keys) to counts 
                                (values) of how many times that word appears
        threshold (int): A threshold indicating the lower bound (inclusive)
                         for how many times the corresponding word must appear
                         to be included in the output list

    Output (list[str]): A list of words that appeared at least a threshold 
                        number of times, sorted lexicographically
    """
    ### YOUR CODE HERE


# Exercise 7
def process_line(line):
    """
    Given a line of lyrics from a song, separate it (using spaces as the only 
    valid word boundary) into a list of words. Start the list with the 
    additional string "[START]" and end the list with the string "[END]" so 
    that our subsequent model can reproduce the start and end of lines.

    Input:
        line (str): A line of lyrics from a song

    Output (list[str]): A list of individual words from that line, but with 
                        "[START]" and "[END]" added to the beginning and end 
                        of the list, respectively, to indicate the start and 
                        end of a line
    """
    ### YOUR CODE HERE


# Exercise 8
def markov_counts(lyrics):
    """
    Given a list of lists of song lyrics (of the form read in by the 
    load_lyrics() function), return a dictionary of dictionaries. The outer 
    dictionary maps each word (keys) to an inner dictionary, which represents
    the words that follow it (keys) and the counts (values) of how many times 
    that second word follows the first word in the song lyrics.

    Input:
        lyrics (list[list[str]]): A list of lists of song lyrics of the form 
                                  read in by load_lyrics(). Specifically, the
                                  second value in each inner list represents 
                                  song lyrics, while the first represents the 
                                  location in a song and can be ignored

    Output (dict[dict[str,int]]): A mapping from words to dictionaries of 
                                  words (keys) and counts (values)
    """
    ### YOUR CODE HERE
    

# Exercise 9
def counts_to_probs(next_words):
    """
    Given a dictionary mapping words to counts (of the form of the inner 
    dictionaries in Exercise 8), return a list of tuples of the form 
    (word, lb, ub) that represents a word and a lower bound (lb) and upper 
    bound (ub) for that word. All lower and upper bounds will fall between 
    0.0 (inclusive) and 1.0 (exclusive), and the bounds for each word 
    will be non-overlapping. The list must be sorted lexicographically by 
    the word before assigning the bounds.

    Input:
        next_words (dict[str,int]): A dictionary mapping words (keys) to 
                                    counts (values)

    Output (list[tuple[str,float,float]]): A list of tuples each containing a
                                           word (str), a lower bound (float), 
                                           and an upper bound (float)
    """
    ### YOUR CODE HERE


# Exercise 10
def swiftomatic(model, num_words, seed):
    """
    Given a dictionary representing a Markov chain model (in the format 
    returned by Exercise 8), produce num_words words (or equivalent)
    of pseudorandomly generated lyrics using that Markov chain. Set the seed 
    of Python's pseudorandom number generator to the seed provided to ensure 
    everyone produces the same lyrics, and only call random.random() once 
    per word for the same reason.

    Input:
        model (dict[dict[str,int]]): A dictionary representing a Markov chain
        num_words (int): The number of words to generate using the Markov chain
        seed (int): A seed for the random number generator

    Output (str): The pseudorandomly generated song lyrics
    """
    # Do not remove the following line, which initializes the pseudorandom
    # number generator based on the seed parameter
    random.seed(seed)
    ### YOUR CODE HERE
