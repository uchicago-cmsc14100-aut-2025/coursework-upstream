"""
CMSC 14100
Autumn 2025
Homework #8

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


class ListSpeller:
    """
    Class for a list-based speller
    """

    def __init__(self):
        '''
        Constructor

        Parameters:
          none

        Initialize empty list of words.
        '''
        self.wordlist = []

    def add(self, word):
        '''
        Add the word to the speller if it consists only of lowercase
        letters and is not already present.

        Parameters:
          word : str

        Returns: (does not return a value)
        '''
        # Your Code Here
        return None

    def add_from_file(self, filename):
        '''
        Read the named file, add words (one per line in file).

        Parameters:
          filename : str

        Returns: (does not return a value)
        '''
        # Your Code Here
        return None

    def is_word(self, word):
        '''
        Check presence of given word in the list.

        Parameters:
          word : str

        Returns: boolean
        '''
        # Your Code Here
        return None

    def complete(self, prefix):
        '''
        Return all completions given prefix. The returned list is not
        guaranteed to be in any particular order.

        Parameters:
          prefix : str

        Returns: list[str]
        '''
        # Your Code Here
        return None

    def num_starting(self, prefix):
        '''
        Return the number of completions given prefix.

        Parameters:
          prefix : str

        Returns: int
        '''
        # Your Code Here
        return None

    def num_next(self, prefix):
        '''
        Return the number of next letters given prefix.

        Parameters:
          prefix : str

        Returns: int
        '''
        # Your Code Here
        return None

    def list_words(self):
        '''
        Return all the words in the list. Returned list not
        guaranteed in any particular order.

        Parameters:
          none

        Returns: list[str]
        '''
        # Your Code Here
        return None

    def num_words(self):
        '''
        Return the number of words in the list.

        Parameters:
          none

        Returns: int
        '''
        # Your Code Here
        return None
