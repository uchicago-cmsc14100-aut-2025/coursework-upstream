"""
CMSC 14100
Autumn 2025
Homework #7

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

"""
Requirements:
1. The `Duration` class should have:
   - A `mins` (int), a whole number of minutes
   - A `secs` (int), a number of seconds beyond the whole minute, 0 <= secs <= 59

2. The `Song` class should have:
   - A `title` (str)
   - An `artist` (str)
   - A `length` (Duration)
   - An `owned` (bool)
   - A `play_count` (int, starts at 0)

3. The `Playlist` class should have:
   - A `name` (str)
   - A `songs` (list(Song))
"""

class Duration:
    """Represents a duration of time (minutes and seconds)."""

    def __init__(self, mins, secs):
        """
        Constructor for Duration.

        Input:
            mins (int): The number of whole minutes.
            secs (int): The number of seconds beyond the whole minute, 0 <= secs <= 59.
        """
        # Your Code Here
        return None

    def in_seconds(self):
        """
        Returns the duration expressed as a total number of seconds.

        Input:
            None

        Output (int): the total number of seconds in the duration.
        """
        # Your Code Here
        return None

    def __add__(self, other):
        """
        Adds two durations.

        Input:
            other (Duration): The other Duration to sum.

        Output (Duration): The sum of the two durations.
        """
        # Your Code Here
        return None

    def __str__(self):
        """
        Generates string representation of the object

        Input:
            None

        Output (str): string in format M:SS.
        """
        # Your Code Here
        return None

    def __repr__(self):
        """
        Generates Python syntax representation of the object

        Input:
            None

        Output (str): string in format Duration(M, S).
        """
        # Your Code Here
        return None

    def __eq__(self, other):
        """
        Returns whether two durations are equal.

        Input:
            other (Duration): The other Duration to which to compare.

        Output (bool): Whether the durations are equal.
        """
        # Your Code Here
        return None

    def __lt__(self, other):
        """
        Returns whether a duration is less than another.

        Input:
            other (Duration): The other Duration to which to compare.

        Output (bool): Whether this duration is less than the other.
        """
        # Your Code Here
        return None

    def __le__(self, other):
        """
        Returns whether a duration is less than or equal to another.

        Input:
            other (Duration): The other Duration to which to compare.

        Output (bool): Whether this duration is less than or equal to the other.
        """
        # Your Code Here
        return None


class Song:
    """Represents a song, tracking metadata, length, and ownership."""

    def __init__(self, title, artist, length, owned):
        """
        Constructor for Song

        Input:
            title (str): The name of the song.
            artist (str): The credited artist for the song.
            length (Duration): The length of the song.
            owned (bool): Whether the song is owned.
        """
        # Your Code Here
        return None

    def play(self, costs):
        """
        Reflects playing the song once and updates the play count,
        returning the cost of doing so.

        Input:
            costs (dict[str, int]): The costs of playing a song.
                                    costs["per_play"]: per-play cost
                                    costs["per_second"]: per-second cost
                                    (both must be present; one or both may be zero)

        Output (int): The cost of playing the song
        """
        # Your Code Here
        return None

    def __str__(self):
        """
        Generates string representation of the object

        Input:
            None

        Output (str): string in format "Title, by Artist (M:SS)".
        """
        # Your Code Here
        return None


class Playlist:
    """Represents a playlist of songs."""

    def __init__(self, name, songs):
        """
        Constructor for Playlist class.

        Input:
            name (str): The name of the playlist.
            songs (list[Song]): The songs comprising the playlist.
        """
        # Your Code Here
        return None

    def total_length(self):
        """
        Returns the duration of the playlist.

        Input:
            None

        Output (Duration): The duration of all the songs.
        """
        # Your Code Here
        return None

    def play(self, costs):
        """
        Plays the list and returns the total cost incurred in so doing.

        Input:
            costs (dict[str, int]): The costs of playing a song.
                                    costs["per_play"]: per-play cost
                                    costs["per_second"]: per-second cost
                                    (both must be present; one or both may be zero)

        Output (int): The cost of playing all the songs.
        """
        # Your Code Here
        return None

    def artist_counts(self):
        """
        Counts the occurrences of each artist in the playlist.

        Input:
            None

        Output (dict): A dictionary mapping artist name to song count.
        """
        # Your Code Here
        return None

    def first_part(self, limit):
        """
        Makes a playlist consisting of the first however many songs that, taken together,
        do not exceed the specified duration.
        
        Input:
            limit (Duration): Max duration of resulting playlist.

        Output (Playlist): The playlist, limited by duration.
        """
        # Your Code Here
        return None

    def __str__(self):
        """
        Generates string representation of the object

        Input:
            None

        Output (str): string in format Name (x songs, M:SS).
        """
        # Your Code Here
        return None
