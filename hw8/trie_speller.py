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

class Trie:
    """
    Class for representing tries
    """

    def __init__(self, root):
        '''
        Constructor

        Parameters:
         root : str (a character, but Python does not have a "char" type)

        Initialize root to given char, empty dict of children, final to False.
        '''
        self.root = root
        self.children = {}
        self.final = False

    def add(self, word):
        '''
        Add the word to the trie.

        Parameters:
	     word : str

        Returns: (does not return a value)
        '''
        # Your Code Here
        return None

    def is_word(self, word):
        '''
        Check presence of given word in the trie.

        Parameters:
         word : str

        Returns: boolean
        '''
        # Your Code Here
        return None

    def list_words(self):
        '''
        Return all the words in the trie. Returned list not guaranteed
        in any particular order.

        Parameters:
         none

        Returns: list[str]
        '''
        # Your Code Here
        return None

    def num_words(self):
        '''
        Return the number of words in the trie.

        Parameters:
          none

        Returns: int
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

    def _compl(self, prefix, acc):
        '''
        Private method. Return all completions given prefix. The
        parameter acc stores the string seen thus far in traversal of
        the trie. The returned list is not guaranteed to be in any
        particular order.

        Parameters:
          prefix : str
          acc : str

        Returns: list[str]
        '''
        # Your Code Here
        return None

    def num_starting(self, prefix):
        '''
        Return the number of completions of the given prefix.

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


class TrieSpeller:
    """
    Class for a trie-based speller
    """

    def __init__(self):
        '''
        Constructor

        Parameters:
          none

        Initialize dictionary of empty tries, one per letter.
        '''
        self.tries = {}
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.tries[char] = Trie(char)

    def add(self, word):
        '''
        Add the word to the trie if it consists only of lowercase
        letters.

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
        Check presence of given word in the object.

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
        Return all the words in the object. Returned list not
        guaranteed in any particular order.

        Parameters:
          none

        Returns: list[str]
        '''
        # Your Code Here
        return None

    def num_words(self):
        '''
        Return the number of words in the object.

        Parameters:
          none

        Returns: int
        '''
        # Your Code Here
        return None
