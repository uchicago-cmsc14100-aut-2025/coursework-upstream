"""
CMSC 14100
Autumn 2025

Test code for Homework #2
"""
import hw2
import os
import sys

import math
import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw2"

@pytest.mark.parametrize("a, x, expected",
                         [(0, 0, 0),
                          (5, 2, 12),
                          (5, 0, 0),
                          (9, 1, 10),
                          (9, -2, -20),
                          (-11, 2, -20)])
def test_add_one_and_multiply(a, x, expected):
    """
    Do a single test for Exercise 1: add_one_and_multiply
    """
    steps = [f"actual = hw2.add_one_and_multiply({a}, {x})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.add_one_and_multiply(a, x)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("u, v, expected",
                         [("a", "b", False),
                          ("a", "a", False),
                          ("", "", False),
                          ("cy", "ycc", False),
                          ("catca", "tcat", True),
                          ("burb", "burb", False),
                          ("burbb", "brub", True),
                          ("burb", "bRub", False),
                          ("a b c ", "c b a", True),
                          (" ", "", True)])
def test_longer_string(u, v, expected):
    """
    Do a single test for Exercise 2: longer_string
    """
    steps = [f"actual = hw2.longer_string({u}, {v})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.longer_string(u, v)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a, b, c, t, expected",
                         [(0,0,0,0,0),
                          (3,3,3,1,1),
                          (4,4,4,1,8),
                          (5,5,5,1,27),
                          (3,4,5,1,6),
                          (4,3,5,1,6),
                          (5,4,3,1,6),
                          (11,5,10,1,216),
                          (11,11,11,1,729),
                          (13,13,13,1,1331),
                          (21,11,31,2,3213)])
def test_box_interior_volume(a, b, c, t, expected):
    """
    Do a single test for Exercise 3: box_interior_volume
    """
    steps = [f"actual = hw2.box_interior_volume({a}, {b}, {c}, {t})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.box_interior_volume(a, b, c, t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("income, expected",
                         [(0,0),
                          (300,90),
                          (50000, 22300),
                          (1000, 300),
                          (2000, 700),
                          (2001, 700),
                          (2100, 745),
                          (1999, 699),
                          (999, 299),
                          (900,270),
                          (1200,380),
                          (1600,540),
                          (2800,1060),
                          (4000,1600),
                          (9000,3850)])
def test_graduated_income_tax(income, expected):
    """
    Do a single test for Exercise 4: graduated_income_tax
    """
    steps = [f"actual = hw2.graduated_income_tax({income})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.graduated_income_tax(income)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)



@pytest.mark.parametrize("height, expected",
                         [(30,0),
                          (31,100),
                          (32,300),
                          (99,0),
                          (100,100),
                          (101,300),
                          (76543,100),
                          (56879,300)])
def test_height_credit(height, expected):
    """
    Do a single test for Exercise 5: height_credit
    """
    steps = [f"actual = hw2.height_credit({height})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.height_credit(height)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("income, charity, height, expected",
                         [(100,0,99,30),
                          (345,675,23,0),
                          (50000,10000,132,17800),
                          (50000,100000,132,0),
                          (3000,3000,133,0),
                          (100,0,100,0),
                          (100,0,101,0),
                          (900,0,120,270),
                          (900,0,121,170),
                          (900,0,122,0),
                          (1000,100,120,270),
                          (1000,100,121,170),
                          (1000,100,122,0),
                          (1000,1000,100,0)])
def test_annual_tax(income, charity, height, expected):
    """
    Do a single test for Exercise 6: annual_tax
    """
    steps = [f"actual = hw2.annual_tax({income}, {charity}, {height})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.annual_tax(income, charity, height)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0,0,0,0),
                          (144,12,63,82),
                          (255,195,0,204),
                          (100,50,200,94),
                          (255,255,255,254),
                          (255,0,0,139),
                          (0,255,0,195),
                          (0,0,255,86),
                          (255,255,0,240),
                          (255,0,255,163),
                          (11,22,33,21),
                          (100,50,200,94)])
def test_luminance(r, g, b, expected):
    """
    Do a single test for Exercise 7: is_valid_color
    """
    steps = [f"actual = hw2.luminance({r}, {g}, {b})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.luminance(r, g, b)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("r, g, b, expected",
                         [(0,0,0,(0,0,0)),
                          (100,50,200,(94,94,94)),
                          (123,123,123,(123,123,123)),
                          (4,4,4,(3,3,3)),
                          (255,255,255,(254,254,254)),
                          (255,0,0,(139,139,139)),
                          (0,255,0,(195,195,195)),
                          (0,0,255,(86,86,86)),
                          (100,50,200,(94,94,94)),
                          (11,22,33,(21,21,21))])
def test_grayscale(r, g, b, expected):
    """
    Do a single test for Exercise 8: grayscale
    """
    steps = [f"actual = hw2.grayscale({r}, {g}, {b})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.grayscale(r, g, b)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)



@pytest.mark.parametrize("r, g, b, expected",
                         [(0,0,0,(0,0,0,1)),
                          (144,12,63,(0,0.91666666,0.5625,0.4352941176)),
                          (255,195,0,(0,0.23529411,1,0)),
                          (255,255,255,(0,0,0,0)),
                          (255,0,0,(0,1,1,0)),
                          (0,255,0,(1,0,1,0)),
                          (0,0,255,(1,1,0,0))])                                                     
def test_rgb_to_cmyk(r,g,b,expected):
    """
    Do a single test for Exercise 9: rgb_to_cmyk
    """
    steps = [f"actual = hw2.rgb_to_cmyk({r}, {g}, {b})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.rgb_to_cmyk(r,g,b)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    #err_msg = helpers.check_result(actual, pytest.approx(expected))
    err_msg = helpers.check_cmyk(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
