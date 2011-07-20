def break_words(stuff):
    """docstring for break_words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """docstring for sort_words"""
    return sorted(words)

def print_first_word(words):
    """docstring for print_first_word"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """docstring for print_last_word"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """docstring for sort_sentence"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """docstring for print_first_and_last"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """docstring for print_first_and_last_sorted"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
