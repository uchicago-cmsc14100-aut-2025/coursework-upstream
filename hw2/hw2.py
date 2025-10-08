import math

"""
CMSC 14100
Autumn 2025
Homework #2

SOLUTIONS
"""

# Exercise 1
def add_one_and_multiply(a, x):
    """
    Add 1 to a, and multiply by x.

    input:
        a (int): an integer value
        x (int): an integer value

    Output (int): The result of adding 1 to a and then multiplying by x.

    Examples:
        >>> add_one_and_multiply(2, 4)
        12
        >>> add_one_and_multiply(-13, 5)
        -60
    """
    ### delete the raise ValueError(...) code and replace with working code
    raise ValueError("todo: add_one_and_multiply")


# Exercise 2
def longer_string(s, t):
    """
    Given two strings s and t, determine whether the first is longer than
    the second.

    input:
        s (str): a string
        t (str): a string

    Output (bool): s is longer than t

    Examples:
        >>> longer_string("a","b")
        False
        >>> longer_string("a","bb")
        False
        >>> longer_string("aaa","bb")
        True

    """
    ### delete the raise ValueError(...) code and replace with working code
    raise ValueError("todo: longer_string")

# Exercise 3
def box_interior_volume(length, width, depth, thickness):
    """
    Compute the volume of the interior of a box, given its outer
    dimensions and the thickness of its walls.

    input:
        length (number)
        width (number)
        depth (number)
        thickness (number)

    Output (number): the interior volume

    Examples:
        >>> box_interior_volume(11,11,11,1)
        729       

    """
    ### delete the raise ValueError(...) code and replace with working code
    raise ValueError("todo: box_interior_volume")

# Exercise 4
def graduated_income_tax(income):
    """
    Income tax is 30% up to $1000, 40% up to $2000, 45% thereafter.

    assert income is a nonnegative number
    
    Input:
      income (int): a number of dollars
        
    Output (int):
      the tax to be paid on the given income

    Examples:
        >>> graduated_income_tax(100)
        30
        >>> graduated_income_tax(200)
        60
    """
    ### delete the raise ValueError(...) code and replace with working code
    raise ValueError("todo: graduated_income_tax")

# Exercise 5
def height_credit(height_cm):
    """
    If your integer height (cm) mod 3 is 0, you get no credit.
    If it is 1 mod 3, you get $100.
    If it is 2 mod 3, you get $300.

    Input:
      height_cm (int)
    
    Output (int):
      tax credit as outlined above
    
    Examples:
        >>> height_credit(100)
        100
        >>> height_credit(210)
        0
    """
    ### delete the raise ValueError(...) code and replace with working code
    raise ValueError("todo: height_credit")

# Exercise 6
def annual_tax(income, charity, height_cm):
    """
    First, charity is subtracted from your income for your
    adjusted income. Your adjusted income cannot be less than 0.

    You must pay the graduated income tax on your adjusted income
    minus your height credit.

    The result must be a nonnegative number (i.e., tax bottoms out at
    0).

    Input:
      income (int) in dollars
      charity (int) in dollars
      height_cm (int)
    
    Output (int):
      graduated tax on adjusted income minus height deduction (>= 0)
    
    Examples:
        >>> annual_tax(500,0,210)
        150
        >>> annual_tax(500,0,211)
        50
    """
    ### delete the raise ValueError(...) code and replace with working code
    raise ValueError("todo: annual_tax")

# Exercise 7
def luminance(r,g,b):
    """
    Compute the luminance per formula in assignment description.

    Input:
        r (int): red 
        g (int): green
        b (int): blue

    Output (int)

    Examples:
        >>> luminance(0,0,0)
        0
        >>> luminance(255,255,255)
        254
    """
    ### delete the raise ValueError(...) code and replace with working code
    raise ValueError("todo: luminance")


# Exercise 8
def grayscale(r,g,b):
    """
    Compute the grayscale of given color based on luminance.

    Input:
        r (int): red
        g (int): green
        b (int): blue

    Output (int,int,int)
        
    Examples:
        >>> grayscale(0,0,0)
        (0,0,0)
        >>> grayscale(255,255,255)
        (254,254,254)
    """
    ### delete the raise ValueError(...) code and replace with working code
    raise ValueError("todo: grayscale")

# Exercise 9
def rgb_to_cmyk(r,g,b):
    """
    Compute the CMYK of given RGB per formula in assignment description.

    Input:
        r (int): red
        g (int): green
        b (int): blue
    
    Output (float,float,float,float)

    Examples:
        >>> rgb_to_cmyk(0,0,0)
        (0,0,0,1)
        >>> rgb_to_cmyk(255,0,0)
        (0.0,1.0,1.0,1.0)
    """
    ### delete the raise ValueError(...) code and replace with working code
    raise ValueError("todo: rgb_to_cmyk")
