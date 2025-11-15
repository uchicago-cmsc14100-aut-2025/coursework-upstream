"""
CMSC 14100
Autumn 2025

Test code for Homework #7
"""
import pytest
import helpers
import sys  
import os



# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw7"

from playlists import *
from hw7 import Duration, Song, Playlist

def same_object(actual_object, expected_object):
    """ Helper function to check if two objects have the same attributes 
    and same values for those attributes"""
    if actual_object is None:
        return ("The Expected an object, got None instead\n"
           f"  Expected: {expected_object}\n"
           f"  Actual: {actual_object}")
    attr1 = vars(actual_object)
    attr2 = vars(expected_object)
    if attr1 != attr2:
        return ("The actual and expected object attributes of the object do not match\n"
           f"  Expected: {attr2}\n"
           f"  Actual: {attr1}")
    
    for attr in dir(expected_object):
        if getattr(actual_object, attr) != getattr(expected_object, attr):
            return (f"The actual and expected value of the {attr} attribute of the object do not match\n"
                    f"  Expected: {getattr(expected_object, attr)}\n"
                    f"  Actual: {getattr(actual_object, attr)}")
    
    return None

def test_duration_constructor():
    """ Test that the Duration constructor works"""
    steps = [
        "dur = hw7.Duration(12, 34)",
        "dur.mins",
        "dur.secs"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur = Duration(12, 34)

        err_msg = helpers.check_result(dur.mins, 12)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(dur.secs, 34)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_in_seconds():
    """ Test that the Duration in_seconds method works"""
    steps = [
        "dur = hw7.Duration(12, 34)",
        "dur.in_seconds()"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur = Duration(12, 34)

        err_msg = helpers.check_result(dur.in_seconds(), 12 * 60 + 34)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_add_simpler():
    """ Test that adding two durations without adding past 59 seconds works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(56, 12)",
        "print(dur1 + dur2)"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(56, 12)
        durs = dur1 + dur2

        err_msg = helpers.check_result(durs.mins, 68)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(durs.secs, 46)
        if err_msg is not None:
            pytest.fail

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_add_complex():
    """ Test that adding two durations with adding past 59 seconds works"""
    steps = [
        "dur1 = hw7.Duration(12, 47)",
        "dur2 = hw7.Duration(34, 23)",
        "print(dur1 + dur2)"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 47)
        dur2 = Duration(34, 23)
        durs = dur1 + dur2

        err_msg = helpers.check_result(durs.mins, 47)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(durs.secs, 10)
        if err_msg is not None:
            pytest.fail

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_str_2digits():
    """ Test that the Duration __str__ method works for minutes with two digits"""
    steps = [
        "dur = hw7.Duration(12, 34)",
        "print(dur)"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur = Duration(12, 34)

        err_msg = helpers.check_result(str(dur), "12:34")
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(dur.secs, 34)
        if err_msg is not None:
            pytest.fail

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_str_1digit():
    """ Test that the Duration __str__ method works for minutes with one digit"""
    steps = [
        "dur = hw7.Duration(10, 09)",
        "print(dur)"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur = Duration(10, 9)

        err_msg = helpers.check_result(str(dur), "10:09")
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(dur.secs, 34)
        if err_msg is not None:
            pytest.fail

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_str_repr():
    """ Test that the Duration __repr__ method works"""
    steps = [
        "dur = hw7.Duration(14, 1)",
        "dur"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur = Duration(14, 1)

        err_msg = helpers.check_result(dur.__repr__(), "Duration(14, 1)")
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(dur.secs, 34)
        if err_msg is not None:
            pytest.fail

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_equal_yes():
    """ Test that comparing two equal Durations works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(12, 34)",
        "dur1 == dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(12, 34)

        err_msg = helpers.check_result(dur1 == dur2, True)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_equal_no_secs():
    """ Test that comparing two non-equal Durations (in the secs) works"""
    steps = [
        "dur1 = Duration(12, 34)",
        "dur2 = Duration(12, 33)",
        "dur1 == dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(12, 33)

        err_msg = helpers.check_result(dur1 == dur2, False)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_equal_no_mins():
    """ Test that comparing two non-equal Durations (in the mins) works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(11, 34)",
        "dur1 == dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(11, 34)

        err_msg = helpers.check_result(dur1 == dur2, False)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_lt_equal():
    """ Test that < on two equal Durations works"""
    steps = [
        "dur1 = Duration(12, 34)",
        "dur2 = Duration(12, 34)",
        "dur1 < dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(12, 34)

        err_msg = helpers.check_result(dur1 < dur2, False)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_lt_yes_secs():
    """ Test that < with a Duration less in the secs works"""
    steps = [
        "dur1 = hw7.Duration(12, 33)",
        "dur2 = hw7.Duration(12, 34)",
        "dur1 < dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 33)
        dur2 = Duration(12, 34)

        err_msg = helpers.check_result(dur1 < dur2, True)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_lt_no_secs():
    """ Test that < with a Duration greater in the secs works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(12, 33)",
        "dur1 < dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(12, 33)

        err_msg = helpers.check_result(dur1 < dur2, False)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_lt_yes_mins():
    """ Test that < with a Duration less in the mins works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(13, 34)",
        "dur1 < dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(13, 34)

        err_msg = helpers.check_result(dur1 < dur2, True)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_lt_no_mins():
    """ Test that < with a Duration greater in the mins works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(11, 35)",
        "dur1 < dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(11, 35)

        err_msg = helpers.check_result(dur1 < dur2, False)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_le_equal():
    """ Test that <= on two equal Durations works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(12, 34)",
        "dur1 <= dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(12, 34)

        err_msg = helpers.check_result(dur1 <= dur2, True)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_le_yes_secs():
    """ Test that <= with a Duration less in the secs works"""
    steps = [
        "dur1 = hw7.Duration(12, 33)",
        "dur2 = hw7.Duration(12, 34)",
        "dur1 <= dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 33)
        dur2 = Duration(12, 34)

        err_msg = helpers.check_result(dur1 <= dur2, True)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_le_no_secs():
    """ Test that < with a Duration greater in the secs works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(12, 33)",
        "dur1 <= dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(12, 33)

        err_msg = helpers.check_result(dur1 <= dur2, False)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_le_yes_mins():
    """ Test that <= with a Duration less in the mins works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(13, 34)",
        "dur1 <= dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(13, 34)

        err_msg = helpers.check_result(dur1 <= dur2, True)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_duration_le_no_mins():
    """ Test that <= with a Duration greater in the mins works"""
    steps = [
        "dur1 = hw7.Duration(12, 34)",
        "dur2 = hw7.Duration(11, 35)",
        "dur1 <= dur2"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        dur1 = Duration(12, 34)
        dur2 = Duration(11, 35)

        err_msg = helpers.check_result(dur1 <= dur2, False)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_song_constructor():
    """ Test that the Song constructor works"""
    steps = [
        'song = hw7.Song("Peace Piece", "Bill Evans", hw7.Duration(6, 44), True)',
        "song.title",
        "song.artist",
        "song.length.mins",
        "song.length.secs",
        "song.owned",
        "song.play_count"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        song = Song("Peace Piece", "Bill Evans", Duration(6, 44), True)

        err_msg = helpers.check_result(song.title, "Peace Piece")
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(song.artist, "Bill Evans")
        if err_msg is not None:
            pytest.fail

        err_msg = helpers.check_result(song.length.mins, 6)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(song.length.secs, 44)
        if err_msg is not None:
            pytest.fail

        err_msg = helpers.check_result(song.owned, True)
        if err_msg is not None:
            pytest.fail

        err_msg = helpers.check_result(song.play_count, 0)
        if err_msg is not None:
            pytest.fail

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_song_play_owned():
    """ Test that playing an owned Song works"""
    steps = [
        'song = hw7.Song("Peace Piece", "Bill Evans", hw7.Duration(6, 44), True)',
        'costs = {"per_play" : 100, "per_second" : 2}',
        "song.play(costs)",
        "song.play_count"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        song = Song("Peace Piece", "Bill Evans", Duration(6, 44), True)
        costs = {"per_play" : 100, "per_second" : 2}

        err_msg = helpers.check_result(song.play(costs), 0)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(song.play_count, 1)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_song_play_streamed():
    """ Test that playing a streamed Song works"""
    steps = [
        'song = hw7.Song("Peace Piece", "Bill Evans", hw7.Duration(6, 44), False)',
        'costs = {"per_play" : 100, "per_second" : 2}',
        "song.play(costs)",
        "song.play_count"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        song = Song("Peace Piece", "Bill Evans", Duration(6, 44), False)
        costs = {"per_play" : 100, "per_second" : 2}

        err_msg = helpers.check_result(song.play(costs), 100 + (6 * 60 + 44) * 2)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
        err_msg = helpers.check_result(song.play_count, 1)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


def test_song_str():
    """ Test that the Song __str__ method works"""
    steps = [
        'song = hw7.Song("Peace Piece", "Bill Evans", hw7.Duration(6, 44), True)',
        "print(song)"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        song = Song("Peace Piece", "Bill Evans", Duration(6, 44), True)

        err_msg = helpers.check_result(str(song), "Peace Piece, by Bill Evans (6:44)")
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
 
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("index, expected_length", 
                          [
                              (0, "78:37"),
                              (1, "51:51"),
                              (2, "35:29"),
                              (3, "63:26"),
                              (4, "37:12")
                          ])
def test_playlist_total_length(index, expected_length):
    """Test the Playlist total_length method"""
    steps = [
        "from playlist import get_playlists",
        f"playlist = get_playlists()[{index}]",
        "print(playlist.total_length())"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        playlist = get_playlists()[index]

        err_msg = helpers.check_result(str(playlist.total_length()), expected_length)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("index, expected_cost", 
                          [
                              (0, 5606),
                              (1, 5866),
                              (2, 0),
                              (3, 6566),
                              (4, 4090)
                          ])
def test_playlist_play(index, expected_cost):
    """Test the Playlist play method"""
    steps = [
        "from playlist import get_playlists",
        f"playlist = get_playlists()[{index}]",
        'costs = {"per_play" : 100, "per_second" : 2}',
        "playlist.play(costs)"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        playlist = get_playlists()[index]
        costs = {"per_play" : 100, "per_second" : 2}

        err_msg = helpers.check_result(playlist.play(costs), expected_cost)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("index, expected_counts", 
                          [
                              (0,
                                  {"Alice Coltrane" : 6,
                                   "Alice Coltrane & Carlos Santana" : 1,
                                   "Joe Henderson & Alice Coltrane" : 1,
                                   "Alice Coltrane & John Coltrane" : 2}
                              ),
                              (1,
                                  {"Bill Evans" : 5,
                                   "Bill Evans Trio" : 2,
                                   "Bill Evans & Tony Bennett" : 1,
                                   "Bill Evans & Jim Hall" : 1,
                                   "Jaden Evans & Bill Evans" : 1}
                              ),
                              (2,
                                  {"Charlie Parker" : 5,
                                   "Charlie Parker Quartet" : 2,
                                   "Charlie Parker & Dizzy Gillespie" : 1,
                                   "Charlie Parker, Dizzy Gillespie, Bud Powell, Max Roach, & Charles Mingus" : 1,
                                   "Charlie Parker and His Orchestra" : 1}
                              ),
                              (3,
                                   {"Miles Davis" : 5,
                                   "Miles Davis All Stars" : 1,
                                   "Miles Davis Quintet" : 2,
                                   "Michel Legrand & Miles Davis" : 1,
                                   "Miles Davis & Milt Jackson" : 1}
                              ),
                              (4,
                                  {"Nina Simone" : 9,
                                   "Billie Holiday, Nina Simone, Ella Fitzgerald, & Duke Ellington" : 1}
                              )
                          ])
def test_playlist_artist_counts(index, expected_counts):
    """Test the Playlist artist_counts method"""
    steps = [
        "from playlist import get_playlists",
        f"playlist = get_playlists()[{index}]",
        "playlist.artist_counts()"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        playlist = get_playlists()[index]

        err_msg = helpers.check_result(playlist.artist_counts(), expected_counts)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("index, expected_str", 
                          [
                              (0, "Alice Coltrane Mix (10 songs, 78:37)"),
                              (1, "Bill Evans Mix (10 songs, 51:51)"),
                              (2, "Charlie Parker Mix (10 songs, 35:29)"),
                              (3, "Miles Davis Mix (10 songs, 63:26)"),
                              (4, "Nina Simone Mix (10 songs, 37:12)")
                          ])
def test_playlist_str(index, expected_str):
    """Test the Playlist __str__ method"""
    steps = [
        "from playlist import get_playlists",
        f"playlist = get_playlists()[{index}]",
        "print(playlist)"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        playlist = get_playlists()[index]

        err_msg = helpers.check_result(str(playlist), expected_str)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("limit_m, limit_s,, expected_num", 
                          [
                              (0, 0, 0),
                              (4, 0, 0),
                              (4, 1, 1),
                              (9, 10, 1),
                              (9, 11, 2),
                              (9, 12, 2),
                              (13, 46, 3),
                              (20, 30, 4),
                              (26, 19, 5),
                              (29, 54, 6),
                              (34, 57, 7),
                              (41, 31, 8),
                              (47, 9, 9),
                              (51, 51, 10),
                              (60, 0, 10)
                          ])
def test_playlist_first_part(limit_m, limit_s, expected_num):
    """Test the Playlist first_part method"""
    steps = [
        "from playlist import get_playlists",
        "playlist = get_playlists()[1]",
        f"print(playlist.first_part(hw7.Duration({limit_m}, {limit_s})))"
    ]

    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        playlist = get_playlists()[1]

        shortened = playlist.first_part(Duration(limit_m, limit_s))

        err_msg = helpers.check_result(len(shortened.songs), expected_num)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

        for i, song in enumerate(shortened.songs):
            err_msg = helpers.check_result(song.title, playlist.songs[i].title)
            if err_msg is not None:
                pytest.fail(err_msg + recreate_msg)
    
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
