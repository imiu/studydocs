# Problem Set 5: 6.00 Word Game
# Name:
# Collaborators:
# Time:
#

import random
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    if len(word) == 0:
        return score
    elif word == '.':
        return score
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    if len(word) == n:
        score += 50
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    for letter in word:
        hand[letter] = hand.get(letter, 0) - 1
        if hand[letter] == 0:
            del hand[letter]
    return hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    if points_dict.get(word) > 0:
        return True
    else:
        return False

#
# Problem #6.3: Get points for words
#
def get_words_to_points(word_list):
    """Return a dict that maps every word in a word_list to its point value."""
    points_dict = {}
    for word in word_list:
        points_dict[word] = get_word_score(word, HAND_SIZE)

    return points_dict

#
# Problem #6.3: Get points for words
#
def pick_best_word(hand, points_dict):
    """Find best word with given hand and points dictionary"""
    word = "."
    score = 0
    best_score = 0
    for tmp_word in points_dict.keys():
        if is_valid_word(tmp_word, hand, points_dict):
            score = get_word_score(tmp_word, HAND_SIZE)
            if score > best_score:
                word = tmp_word
                best_score = score
    return word

#
# Problem #6.4: Get a sequence of letters for a word
#
def get_word_rearrangements(word):
    """Get a string of letters, that are contained in a word"""
    tmp_list = list(word)
    tmp_list.sort()
    sequence = "".join(tmp_list)

    return sequence

#
# Problem #6.4: Get a sequence of letters for a hand
#
def get_hand_rearrangements(hand):
    """ Get a rearrangements for a given hand """
    tmp_list = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            tmp_list.append(letter)
    tmp_list.sort()
    sequence = "".join(tmp_list)

    return sequence

#
# Problem #6.4: Create a rearrangement dictionary
#
def get_rearrange_dic(word_list):
    """Create a list of words as sequences of letter for a word list"""
    rearrange_dict = {}
    for word in word_list:
        rearrange_dict[get_word_rearrangements(word)] = word
    return rearrange_dict

def get_sets_recursive(word, word_list):
    """Generate all possible string from a given, without order changed"""
    if len(word) > 0:
        str_word = "".join(word)
        if str_word not in word_list:
            word_list.append(str_word)
        for letter in word:
            tmp_word = word[:]
            tmp_word.remove(letter)
            if len(tmp_word) > 0 and "".join(tmp_word) not in word_list:
                get_sets_recursive(tmp_word, word_list)
    return word_list

#
# Problem #6.4: Generate all sequences from a word
#
def get_all_hand_sets(word):
    """Generate all possible string from a given, without order changed"""
    word_list = get_sets_recursive(list(word), [])

    return word_list

#
# Problem #6.4: Pick word faster, than ever
#
def pick_best_word_faster(hand, rearrange_dict):
    """Faster version of picking word algorithm"""
    hand_rearrangements = get_hand_rearrangements(hand)
    hand_sets = get_all_hand_sets(hand_rearrangements)
    max_score_word = '.'
    max_score = 0
    score = 0
    word = '.'
    for sub_set in hand_sets:
        if sub_set in rearrange_dict.keys():
            word = rearrange_dict[sub_set]
            score = get_word_score(word, HAND_SIZE)
            if score > max_score:
                max_score_word = word
                max_score = score

    return max_score_word

#
# Problem #6.3: Get timelimit for a computer
#
def get_time_limit(points_dict, k):
    """
    Return the time limit for the computer player as a function of the multiplier k.
    points_dict should be the same dictionary that is created by get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k

#
# Problem #4: Playing a hand
#
def play_hand(hand, points_dict, rearrange_dict):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    total_score = 0
    game_finished = False
    time_limit = get_time_limit(points_dict, 10)
    print "Time limit is set to %0.2f" %time_limit
    total_time = 0
    time_left = 0

    while not game_finished:
        score = 0
        round_start = 0
        round_end = 0
        round_time = 0
        print "Current hand: ",
        display_hand(hand)
        round_start = time.time()
        round_start = time.time()
        word = pick_best_word(hand, points_dict)
        round_end = time.time()
        round_time = round_end - round_start
        print "###################### %s #########################" %word
        print "###################### %d #########################" %get_word_score(word, HAND_SIZE)
        print "###################### %0.5f #########################" %round_time
        round_start = time.time()
        word = pick_best_word_faster(hand, rearrange_dict)
        round_end = time.time()
        round_time = round_end - round_start
        print "###################### %s #########################" %word
        print "###################### %d #########################" %get_word_score(word, HAND_SIZE)
        print "###################### %0.5f #########################" %round_time
        round_end = time.time()
        round_time = round_end - round_start
        total_time += round_time
        time_left = time_limit - total_time
        if word == ".":
            game_finished = True
        elif len(hand) == 0:
            game_finished = True
        elif total_time > time_limit:
            print "Total time exceeds %d seconds" %time_limit
            game_finished = True
        else:
            if is_valid_word(word, hand, points_dict):
                score = get_word_score(word, HAND_SIZE) / round_time
                total_score += score
                print "It took %0.2f seconds to provide an answer." %round_time
                print "You have %0.2f seconds remaining." %(time_left)
                print "%s earned %0.2f points. Total: %0.2f points." %(word, score, total_score)
                hand = update_hand(hand.copy(), word)
            else:
                print "Invalid word, please try again."
                print "You have %0.2f seconds remaining." %(time_left)



    if game_finished:
        print "Total score: %0.2f" %total_score


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
#
def play_game(points_dict, rearrange_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), points_dict, rearrange_dict)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), points_dict, rearrange_dict)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    points_dict = get_words_to_points(word_list)
    rearrange_dict = get_rearrange_dic(word_list)
    play_game(points_dict, rearrange_dict)
