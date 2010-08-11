# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.

def lost_by_word(word, wordlist):
    """Did player lost the game?"""
    if len(word) > 3 and word in wordlist:
        return True
    return False

def lost_by_no_word(word, wordlist):
    for tmp_word in wordlist:
        if word in tmp_word[0:len(word)]:
            print tmp_word
            return False
    return True

def test_lost_by_word(wordlist):
    succeed = True

    word = "eye"
    if lost_by_word(word, wordlist):
        print "Must return False and got True with word " + word
        succeed = False

    word = "banana"
    if not lost_by_word(word, wordlist):
        print "Must return True and got False with word " + word
        succeed = False

    if succeed:
        print "All test passed"
    else:
        print "Failed"

def test_lost_by_no_word(wordlist):
    succeed = True

    word = "zar"
    if not lost_by_no_word(word, wordlist):
        print "Must return True and got False with word " + word
        succeed = False

    word = "pyn"
    if lost_by_no_word(word, wordlist):
        print "Must return False and got True with word " + word
        succeed = False

    if succeed:
        print "All test passed"
    else:
        print "Failed"


def ghost(wordlist):
    print "Welcome to Ghost"
    print "Player 1 goes first."
    game_over = False
    fragment = ''
    current_player = 1

    while not game_over:
        print "Current word fragment: '" + fragment + "'"

        no_letter = True
        while no_letter:
            letter = raw_input("Player " + str(current_player) + " says letter: ")

            if letter not in string.ascii_letters:
                print "A letter please!"
            else:
                no_letter = False

        fragment += letter.lower()
        #print fragment
        if lost_by_word(fragment, wordlist):
            game_over = True
            print "Player " + str(current_player) + " loses because '" + fragment + "' is a word!"
        if lost_by_no_word(fragment, wordlist):
            game_over = True
            print "Player " + str(current_player) + " loses no word begins with " + fragment

        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

        if game_over:
            print "Player " + str(current_player) + " wins!"



wordlist = load_words()
ghost(wordlist)
# test_lost_by_word(wordlist)
# test_lost_by_no_word(wordlist)