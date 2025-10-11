"""
CMSC 14100
Autumn 2025

Test code for Homework #3
"""
import os
import sys
import pytest
import hw3
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw3"

@pytest.mark.parametrize("speed, expected",
                        [(82, 1),
                        (74, 1),
                        (64, 1),
                        (95, 2),
                        (89, 2),
                        (83, 2),
                        (112, 3),
                        (100, 3),
                        (96, 3),
                        (136, 4),
                        (122, 4),
                        (113, 4),
                        (137, 5),
                        (333, 5),
                        (5678, 5),
                        (10, None),
                        (0, None),
                        (100000000, 5)])
def test_categorize_wind_speed(speed, expected):
    """
    Do a single test for Exercise 1: categorize_wind_speed
    """

    steps = [f"actual = hw3.categorize_wind_speed({speed})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.categorize_wind_speed(speed)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    

@pytest.mark.parametrize("speeds, expected",
                        [([30, 40, 50, 60, 70], 1),
                        ([64, 80, 120, 50, 71], 4),
                        ([11, 17, 35, 20, 14], 0),
                        ([10]*100, 0),
                        ([], 0),
                        ([10], 0),
                        ([100], 1),
                        ([64]*100, 100)])
def test_hurricanes_found(speeds, expected):
    """
    Do a single test for Exercise 2: hurricanes_found
    """

    steps = [f"actual = hw3.hurricanes_found({speeds})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.hurricanes_found(speeds)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    

@pytest.mark.parametrize("speeds, expected",
                        [([64, 80, 120, 50, 71], 1),
                        ([96, 100, 150, 143, 50], 4),
                        ([10, 95, 132, 198, 176], 3),
                        ([10]*100, 0),
                        ([], 0),
                        ([10], 0),
                        ([100], 1),
                        ([64]*100, 0),
                        ([96]*100, 100)])
def test_major_hurricanes_found(speeds, expected):
    """
    Do a single test for Exercise 3: major_hurricanes_found
    """

    steps = [f"actual = hw3.major_hurricanes_found({speeds})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.major_hurricanes_found(speeds)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    

@pytest.mark.parametrize("speeds, expected",
                        [([64, 80, 120, 50, 71], 2),
                        ([96, 100, 150, 143, 50], 0),
                        ([10, 22, 95, 34, 76], None),
                        ([], None),
                        ([10], None),
                        ([100], 0),
                        ([100]*10, 0),
                        ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 10)])
def test_first_major_hurricane(speeds, expected):
    """
    Do a single test for Exercise 4: first_major_hurricane
    """

    steps = [f"actual = hw3.first_major_hurricane({speeds})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.first_major_hurricane(speeds)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    

@pytest.mark.parametrize("speeds, expected",
                        [([64, 80, 120, 50, 71], 2),
                        ([96, 100, 150, 143, 50], 3),
                        ([10, 22, 95, 34, 76], None),
                        ([], None),
                        ([10], None),
                        ([100], 0),
                        ([100]*10, 9),
                        ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 10)])
def test_last_major_hurricane(speeds, expected):
    """
    Do a single test for Exercise 5: last_major_hurricane
    """

    steps = [f"actual = hw3.last_major_hurricane({speeds})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.last_major_hurricane(speeds)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    

@pytest.mark.parametrize("season1, season2, expected",
                        [([64, 80, 120, 50, 71], [96, 100, 150, 143, 50], True),
                        ([96, 100, 150, 143, 50], [10, 22, 95, 34, 76], False),
                        ([], [], False),
                        ([60, 70, 80], [60, 70, 80, 90], False),
                        ([60, 70, 80, 90], [60, 70, 80, 90, 100], True),
                        ([10], [10], False),
                        ([10], [100], True),
                        ([100], [100], False),
                        ([], [100], True),
                        ([100], [], False)])
def test_more_storms(season1, season2, expected):
    """
    Do a single test for Exercise 6: more_storms
    """

    steps = [f"actual = hw3.more_storms({season1, season2})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.more_storms(season1, season2)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    

@pytest.mark.parametrize("speeds, expected",
                        [([200, 100, 120, 134, 167], "above_normal"),
                        ([32, 45, 65, 21, 30], "below_normal"),
                        ([320, 256, 225, 233, 236, 123], "extremely_active"),
                        ([2000, 2000, 2000], "extremely_active"),
                        ([0], "below_normal"),
                        ([], "below_normal"),
                        ([96, 96, 96, 96, 96, 96], "extremely_active"),
                        ([64, 64, 64, 64, 64], "near_normal"),
                        ([64, 64, 64, 64], "below_normal"),
                        ([96, 96], "near_normal"),
                        ([96, 96, 96, 96], "above_normal")])
def test_classify_storm_season(speeds, expected):
    """
    Do a single test for Exercise 7: classify_storm_season
    """

    steps = [f"actual = hw3.classify_storm_season({speeds})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.classify_storm_season(speeds)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    

