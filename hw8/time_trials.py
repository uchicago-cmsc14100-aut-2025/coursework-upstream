import time
import sys
import os

# Handle the fact that this code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

from list_speller import ListSpeller
from trie_speller import TrieSpeller

VERBOSE = False

def time_spellers(ls, ts, test_words):

    for (name, speller) in [('ListSpeller',ls), ('TrieSpeller',ts)]:
        print(f'Number of words in {name}: {speller.num_words()}')

    times = {'ListSpeller': [], 'TrieSpeller': []}
    for (name, speller) in [('ListSpeller',ls), ('TrieSpeller',ts)]:
        for word in test_words:
            time0 = time.time()
            b = speller.is_word(word)
            time1 = time.time()
            time_delta = time1-time0
            if VERBOSE:
                print(f'testing if {name} contains "{word}": {b}')
                print(f'{time_delta:.3e}')
            times[name].append(time_delta)

    avg_ls = sum(times["ListSpeller"]) / len(times["ListSpeller"])
    avg_ts = sum(times["TrieSpeller"]) / len(times["TrieSpeller"])

    print()
    if avg_ts < avg_ls:
        pct = ((avg_ls-avg_ts)/avg_ts) * 100
        print(f"On average, the ListSpeller took {pct:.2f}% more time than the TrieSpeller")
    elif avg_ts > avg_ls:
        pct = ((avg_ts-avg_ls)/avg_ls) * 100
        print(f"On average, the TrieSpeller took {pct:.2f}% more time than the ListSpeller")
    else:
        print(f"On average, the TrieSpeller and the ListSpeller performed the same")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        VERBOSE = True

    print('*** Timing spellers with "m-words.txt"\n')

    ls = ListSpeller()
    ts = TrieSpeller()

    ls.add_from_file('m-words.txt')
    ts.add_from_file('m-words.txt')

    time_spellers(ls, ts, ['mistletoe', 'molasses', 'meteor'])

    print('\n*** Timing spellers with "web2.shuf" (this might take a while)\n')

    ls = ListSpeller()
    ts = TrieSpeller()

    if VERBOSE:
        print('building ListSpeller...')
    # We're going to cheat here and create the words list
    # directly, bypassing add, so we don't have to
    # check for duplicates, etc. Otherwise it takes
    # too long to build the speller!
    with open('web2.shuf') as f:
        set_words = set()
        for word in f.readlines():
            word = word.strip()
            if word.islower():
                set_words.add(word)
        ls.wordlist = list(set_words)

    if VERBOSE:
        print('done building ListSpeller')
        print('building TrieSpeller...')

    ts.add_from_file('web2.shuf')

    if VERBOSE:
        print('done building TrieSpeller')

    time_spellers(ls, ts, ['mistletoe', 'molasses', 'meteor', 'aardvark', 'zoology', 'rapscallion', 'xxxyyy'])

