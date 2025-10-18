"""
CMSC 14100
Autumn 2025
Homework #4

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Utility function to read passwords into a list
from hw4_texts import load_text


# Exercise 1
def reverse_password(password):
    """
    Given a password, reverse it so that it's backwards

    Input:
        password (str): password to be processed

    Output (str): the password returned reversed (i.e., backwards)
    """
    ### YOUR CODE HERE


# Exercise 2
def purge(password, purge_char):
    """
    Given a password, remove (purge) every instance of a specified character.

    Input:
        password (str): password to be processed
        purge_char (str): the character to be purged
        
    Output (str): the password without any instances of the specified character
    """
    ### YOUR CODE HERE


# Exercise 3
def substitute(password, old_char, new_char):
    """
    Given a password, replace every instance of a specified character
    with a specified replacement

    Input:
        password (str): password to be processed
        old_char (str): the character to be replaced
        new_char (str): the character that replaces old_char
        
    Output (str): the password with the specified substitutions made
    """
    ### YOUR CODE HERE


# Exercise 4
def alpha_only(password):
    """
    Given a password, remove all numbers and symbols, leaving only letters.

    Input:
        password (str): password to be processed

    Output (str): the password with numbers and symbols removed
    """
    ### YOUR CODE HERE


# Exercise 5
def toggle_case(password):
    """
    Given a password, toggle the case of all letters by converting each 
    uppercase letter to the corresponding lowercase letter, and vice versa.

    Input:
        password (str): password to be processed

    Output (str): the password with the case toggled as specified
    """
    ### YOUR CODE HERE


# Exercise 6
def shift_numbers(password, shift):
    """
    Given a password, shift all numbers by a specified value.
    For example, 3 shifted by 2 would be 5, while 9 shifted by -3 would be 6.
    Wrap values around. For example, 9 shifted by 1 would be 0, 
    8 shifted by 3 would be 1, and 1 shifted by -2 would be 9.

    Input:
        password (str): password to be processed
        shift (int): an integer ([-9, 9]) indicating the amount
                     by which to shift numbers

    Output (str): the password with numbers shifted as specified
    """
    ### YOUR CODE HERE


# Exercise 7
def length_distribution(credentials):
    """
    Given a list of credentials, return the distribution of the lengths of
    the passwords. Specifically, return a list indicating the number of 
    passwords of lengths 0 through 15, as well as of length 16 or greater.

    Input:
        credentials (list): a list of credentials in the following form:
                            email_address:password
                            (You may assume that neither email addresses
                            nor passwords contain a colon)

    Output (list): a list of size 17 where the first 16 elements (zero-indexed)
    report the number of passwords of length 0 to 15, respectively. The 17th
    element reports the number of passwords of length 16 or greater
    """
    ### YOUR CODE HERE


# Exercise 8
def digit_distribution(credentials):
    """
    Given a list of credentials, return the distribution of the numbers
    (digits) appearing in total across the passwords. Be sure to exclude
    any digits that appear in email addresses.

    Input:
        credentials (list): a list of credentials in the following form:
                            email_address:password
                            (You may assume that neither email addresses
                            nor passwords contain a colon)

    Output (list): a list of size 10 where the i'th element (zero-indexed) 
                   indicates how many times the digit i appeared across all
                   passwords in the provided list of credentials
    """
    ### YOUR CODE HERE


# Exercise 9
def solitary_digits(credentials):
    """
    Given a list of credentials, return the distribution of the numbers
    (digits) appearing in total across only passwords that contain a 
    single digit (potentially in addition to letters and symbols). 
    Be sure to exclude any digits that appear in email addresses.

    Input:
        credentials (list): a list of credentials in the following form:
                            email_address:password
                            (You may assume that neither email addresses
                            nor passwords contain a colon)

    Output (list): a list of size 10 where the i'th element (zero-indexed) 
                   indicates how many times the digit i appeared across all
                   passwords containing only a single digit in the provided 
                   list of credentials
    """
    ### YOUR CODE HERE


# Exercise 10
def matching_passwords(credentials, search_string):
    """
    Given a list of credentials, return the number of passwords that include 
    a given string (case-insensitive) as part or all of the password

    Input:
        credentials (list): a list of credentials in the following form:
                            email_address:password
                            (You may assume that neither email addresses
                            nor passwords contain a colon)
        search_string (str): the string being searched for in the passwords

    Output (int): the number of passwords that contain the search string
    """
    ### YOUR CODE HERE


# Exercise 11
def l33tify(credentials):
    """
    Given a list of credentials, apply "l33t" transformations to all 
    passwords, returning a list of credentials in the same order 
    with those transformations applied to the passwords. Exclude from 
    this list all passwords for which "l33t" transformations did not
    apply

    Input:
        credentials (list): a list of credentials in the following form:
                            email_address:password
                            (You may assume that neither email addresses
                            nor passwords contain a colon)

    Output (list): a list of credentials with "l33t" transformations applied 
                   to all passwords. This list must not include passwords 
                   unchanged from these transformations
    """
    ### YOUR CODE HERE


# Exercise 12
def letters_digits(credentials):
    """
    Given a list of credentials, return the number of passwords that consist
    of letters followed by digits

    Input:
        credentials (list): a list of credentials in the following form:
                            email_address:password
                            (You may assume that neither email addresses
                            nor passwords contain a colon)

    Output (int): the number of passwords of the strict form containing 
                  letters followed by digits
    """
    ### YOUR CODE HERE


