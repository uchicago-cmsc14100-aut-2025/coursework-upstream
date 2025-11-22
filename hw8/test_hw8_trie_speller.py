import sys
import os
import random

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

from trie_speller import TrieSpeller

def test_add_1():
    do_test_add(word='hello')

def test_add_2():
    do_test_add(word='goodbye')

def test_add_3():
    do_test_add(word='marzipan')
    
def test_adds_1():
    do_test_adds(words=["a"])

def test_adds_2():
    do_test_adds(words=["a","bb","ba"])

def test_adds_3():
    do_test_adds(words=["a","bb","ba","bc","ca","ccc","cc","cdcc","cdd","q","r","t"])

def test_add_from_file_1(tmp_path):
    do_test_add_from_file(words=['x'], tmp_path=tmp_path)

def test_add_from_file_2(tmp_path):
    do_test_add_from_file(words=['a','b','c'], tmp_path=tmp_path)

def test_add_from_file_3(tmp_path):
    do_test_add_from_file(words=['a','a','b','c'], tmp_path=tmp_path)

def test_add_from_file_4(tmp_path):
    do_test_add_from_file(words=['a','a:','b','b:','c','c:'], tmp_path=tmp_path)
    
def test_is_word_1():
    do_test_is_word(words=[],sought="banana",result=False)

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

def test_complete_1():
    do_test_complete(words=[],prefix="a",result=[])

def test_complete_2():
    do_test_complete(words=["a"],prefix="a",result=["a"])

def test_complete_3():
    do_test_complete(words=["b"],prefix="a",result=[])

def test_complete_4():
    do_test_complete(words=["a","aa","b","bc"],prefix="a",result=["a","aa"])

def test_complete_5():
    do_test_complete(words=["a","aa","b","bc"],prefix="b",result=["b","bc"])

def test_complete_6():
    do_test_complete(words=["a","aa","b","bc"],prefix="aa",result=["aa"])

def test_complete_7():
    do_test_complete(words=["a","aa","b","bc"],prefix="aaa",result=[])

def test_complete_8():
    do_test_complete(words=["a","aa","b","bc"],prefix="c",result=[])

def test_num_starting_1():
    do_test_num_starting(words=[],prefix="a",result=0)

def test_num_starting_2():
    do_test_num_starting(words=["a"],prefix="a",result=1)

def test_num_starting_3():
    do_test_num_starting(words=["a","ab","b"],prefix="a",result=2)

def test_num_starting_4():
    do_test_num_starting(words=["a","ab","b"],prefix="b",result=1)

def test_num_starting_5():
    do_test_num_starting(words=["a","ab","b"],prefix="x",result=0)

def test_num_next_1():
    do_test_num_next(words=[],prefix="a",result=0)

def test_num_next_2():
    do_test_num_next(words=["a"],prefix="a",result=0)

def test_num_next_3():
    do_test_num_next(words=["a","ab","ac"],prefix="a",result=2)

def test_num_next_4():
    do_test_num_next(words=["a","ab","ac", "abe", "ace", "ad"],prefix="a",result=3)

def test_num_next_5():
    do_test_num_next(words=["a","abcdef","ad","abcdabcd",
                            "abcdbcd","abcdz","abcd","abcda"],
                     prefix="abcd",result=4)

def test_list_words_1():
    do_test_list_words(words=[],result=[])

def test_list_words_2():
    do_test_list_words(words=["a"],result=["a"])

def test_list_words_3():
    do_test_list_words(words=["a","c","b"],result=["a","b","c"])

def test_list_words_4():
    do_test_list_words(words=["a","a","c","b"],result=["a","b","c"])

def test_list_words_5():
    do_test_list_words(words=["a","a","c","c","b","b"],result=["a","b","c"])

def test_list_words_6():
    do_test_list_words(words=["a","c","b","X"],result=["a","b","c"])

def test_list_words_7():
    do_test_list_words(words=["a","c","b","@"],result=["a","b","c"])

def test_list_words_8():
    do_test_list_words(words=["Xa","Xc","Xb","X@"],result=[])

def test_num_words_1():
    do_test_num_words(words=[],result=0)

def test_num_words_2():
    do_test_num_words(words=["a"],result=1)

def test_num_words_3():
    do_test_num_words(words=["a","c","b"],result=3)

def test_num_words_4():
    do_test_num_words(words=["a","a","c","b"],result=3)

def test_num_words_5():
    do_test_num_words(words=["a","a","c","c","b","b"],result=3)

def test_num_words_6():
    do_test_num_words(words=["a","c","b","X"],result=3)

def test_num_words_7():
    do_test_num_words(words=["a","c","b","@"],result=3)

def test_num_words_8():
    do_test_num_words(words=["Xa","Xc","Xb","X@"],result=0)

    
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


def all_lower(s):
    for c in s:
        if not(c.islower()):
            return False
    return True
    
# # #
#
# TEST HELPERS
#
# # #


def do_test_add(word):
    ts = TrieSpeller()
    ts.add(word)
    assert ts.is_word(word)

def do_test_adds(words):
    ts = TrieSpeller()
    for word in words:
        ts.add(word)
    for word in words:
        assert ts.is_word(word)

def do_test_add_from_file(words, tmp_path):
    filename = tmp_path / "words.txt"
    filename.write_text("\n".join(words))

    ts = TrieSpeller()
    ts.add_from_file(str(filename))

    lowercase_words = filter(all_lower, words)
    assert sorted(list(set(lowercase_words))) == sorted(ts.list_words())
    
def do_test_is_word(words, sought, result):
    ts = TrieSpeller()
    for word in words:
        ts.add(word)
    assert ts.is_word(sought)==result

def do_test_complete(words, prefix, result):
    ts = TrieSpeller()
    for word in words:
        ts.add(word)
    assert sorted(ts.complete(prefix)) == sorted(result)

def do_test_num_starting(words, prefix, result):
    ts = TrieSpeller()
    for word in words:
        ts.add(word)
    assert ts.num_starting(prefix)==result

def do_test_num_next(words, prefix, result):
    ts = TrieSpeller()
    for word in words:
        ts.add(word)
    assert ts.num_next(prefix)==result

def do_test_list_words(words, result):
    ts = TrieSpeller()
    for word in words:
        ts.add(word)
    assert sorted(ts.list_words()) == sorted(result)

def do_test_num_words(words, result):
    ts = TrieSpeller()
    for word in words:
        ts.add(word)
    assert ts.num_words() == result

