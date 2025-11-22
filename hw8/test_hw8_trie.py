import sys
import os
import random

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

from trie_speller import Trie

def test_add_1():
    do_test_add(word='hello')

def test_add_2():
    do_test_add(word='goodbye')

def test_add_3():
    do_test_add(word='marzipan')
    
def test_adds_1():
    do_test_adds(words=["a"])

def test_adds_2():
    do_test_adds(words=["a","abb","aba"])

def test_adds_3():
    do_test_adds(words=["a","abb","aba","abc","aca","accc","acc","acdcc","acdd","aq","ar","at"])

def test_is_word_1():
    do_test_is_word(words=["b"],sought="banana",result=False)

def test_is_word_2():
    do_test_is_word(words=["banana"],sought="banana",result=True)

def test_is_word_3():
    do_test_is_word(words=["ban"],sought="banana",result=False)

def test_is_word_4():
    do_test_is_word(words=["ban","banana"],sought="banana",result=True)

def test_is_word_5():
    do_test_is_word(words=["ban","banana"],sought="ban",result=True)

def test_is_word_6():
    do_test_is_word(words=["apple"],sought="banana",result=False)

def test_is_word_7():
    do_test_is_word(words=["boomerang"],sought="banana",result=False)

def test_is_word_8():
    do_test_is_word(words=["banana"],sought="carrot",result=False)

def test_complete_1():
    do_test_complete(words=["x"],prefix="a",result=[])

def test_complete_2():
    do_test_complete(words=["a"],prefix="a",result=["a"])

def test_complete_3():
    do_test_complete(words=["a","aa","ab","abc"],prefix="a",result=["a","aa","ab","abc"])

def test_complete_4():
    do_test_complete(words=["a","aa","ab","abc"],prefix="b",result=[])

def test_complete_5():
    do_test_complete(words=["a","aa","b","bc"],prefix="aa",result=["aa"])

def test_complete_6():
    do_test_complete(words=["a","aa","b","bc"],prefix="aaa",result=[])

def test_complete_7():
    do_test_complete(words=["a","aa","b","bc"],prefix="c",result=[])

def test_list_words_1():
    do_test_list_words(words=["a"],result=["a"])

def test_list_words_2():
    do_test_list_words(words=["a","ac","ab"],result=["a","ab","ac"])

def test_list_words_3():
    do_test_list_words(words=["a","a","ac","ab"],result=["a","ab","ac"])

def test_list_words_4():
    do_test_list_words(words=["a","a","ac","ac","ab","ab"],result=["a","ab","ac"])

def test_num_words_1():
    do_test_num_words(words=["a"],result=1)

def test_num_words_2():
    do_test_num_words(words=["a","ac"],result=2)

def test_num_words_3():
    do_test_num_words(words=["a","ac","ab"],result=3)

def test_num_words_4():
    do_test_num_words(words=["a","a","ac","ab"],result=3)

def test_num_words_5():
    do_test_num_words(words=["a","a","ac","ac","ab","ab"],result=3)
    
# # #
#
# HELPER FUNCTIONS
#
# # #

def gen_recreate_msg(module, function, *params):
    params_str = ", ".join([str(p) for p in params])

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  {}.{}({})".format(module, function, params_str)

    return recreate_msg


def check_none(actual, recreate_msg=None):
    msg = "The function returned None."
    msg += " Did you forget to replace the placeholder value we provide?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg


def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The function returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg


def check_equals(actual, expected, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg


def check_list_unmodified(param_name, before, after, recreate_msg=None):
    msg = "You modified the contents of {} (this is not allowed).\n".format(param_name)
    msg += "  Value before your code: {}\n".format(before)
    msg += "  Value after your code:  {}".format(after)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert before == after, msg
    
# # #
#
# TEST HELPERS
#
# # #


def do_test_add(word):
    t = Trie(word[0])
    t.add(word)
    assert t.is_word(word)

def do_test_adds(words):
    t = Trie(words[0][0])
    for word in words:
        t.add(word)
    for word in words:
        assert t.is_word(word)

def do_test_is_word(words, sought, result):
    t = Trie(words[0][0])
    for word in words:
        t.add(word)
    assert t.is_word(sought)==result

def do_test_complete(words, prefix, result):
    t = Trie(words[0][0])
    for word in words:
        t.add(word)
    compl = t.complete(prefix)
    assert sorted(compl)==sorted(result)

def do_test_list_words(words, result):
    t = Trie(words[0][0])
    for word in words:
        t.add(word)
    assert sorted(t.list_words()) == sorted(result)

def do_test_num_words(words, result):
    t = Trie(words[0][0])
    for word in words:
        t.add(word)
    assert t.num_words() == result

