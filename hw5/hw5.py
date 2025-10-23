"""
CMSC 14100
Autumn 2025
Homework #5

We will be using anonymous grading, so please do NOT include your name anywhere
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.

What can I use?
    You are allowed and encouraged to use basic python constructs and operations. You may NOT import and use any outside libraries or modules. 
    (i.e. statistics, numpy, additional functions from math, etc)
"""
import hw5
from hw5_tables import *
from math import sqrt

# Exercise 1
def extract_column(table, column):
    """
    Produce a list of values in the given column from the given table.

    Input:
        table (list[list]): table of data
        column (str): name of column

    Output (list): list of column data
    """
    raise ValueError("todo")


# Exercise 2
def instances_in_column(table, value, column):
    """
    Count how many times a given value appears in a given column.

    Input:
        table (list[list]): table of data
        value (int | str | float): value to find in column
        column (str): name of column

    Output (int): number of times the value appears
    """
    raise ValueError("todo")


# Exercise 3
def select_columns(table, columns):
    """
    Produce a new table that consists of the given columns from the given table.

    Input:
        table (list[list]): table of data
        columns (list[str]): list of column names

    Output (list[list]): new table with given columns
    """
    raise ValueError("todo")


# Exercise 4
def column_mean(table, column):
    """
    Produce the mean of the values of a numeric column.

    Input:
        table (list[list]): table of data
        column (str): name of column
    
    Output (float): Mean of values in column
    """
    raise ValueError("todo")


# Exercise 5
def column_std_dev(table, column):
    """
    Produce the standard deviation of the values of a numeric column.

    Input:
        table (list[list]): table of data
        column (str): name of column
    
    Output (float): Standard deviation of values in column
    """
    raise ValueError("todo")


# Exercise 6
def filter_exact(table, value, column):
    """
    Search for a value in a column, and produce a new table that consists of only the rows in which the value is present.

    Input:
        table (list[list]): table of data
        value (str): value to find
        column (str): column name

    Output (list[list]): new table with given columns
    """
    raise ValueError("todo")


# Exercise 7
def add_row_sum_column(table, columns, name):
    """
    Extend the table with a new column with given name that contains the sum
    of the values in the specified columns for each row.

    Input:
        table (list[list]): table of data
        columns (list[str]): list of column names
        name (str): name of new column

    Output (None): None, mutates table
    """
    raise ValueError("todo")


# Exercise 8
def identify_outliers(table, column, name):
    """
    Extend the table with a new column with given name that contains boolean values indicating, for each row, whether the value in the given column is an outlier within that column.

    Input:
        table (list[list]): table of data
        column (str): column name
        name (str): name of new column

    Output (None): None, mutates table
    """
    raise ValueError("todo")


# Exercise 9
def column_join(table, columns, delimiter):
    """
    Produce a list of values which are the values in the given columns, joined using the provided delimiter between each value.

    Input:
        table (list[list]): table of data
        column (list[str]): list of column names
        delimiter (str): delimiter between values

    Output (list[str]): new list of joined values
    """
    raise ValueError("todo")

