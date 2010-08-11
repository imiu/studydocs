from string import *


def count_sub_string_match(target, key):
    """Find all occurrences of a string in another"""
    counter = 0
    position = 0
    pointer = 0
    while(pointer < len(target)):
        position = find(target, key, pointer)
        if position != -1:
            counter += 1
            pointer = position + 1
        else:
            pointer += 1
    return counter


def count_sub_string_match_recursive(target, key):
    """Find all occurrences of a string in another with recursion"""
    counter = 0
    position = 0
    position = find(target, key)
    if position == -1:
        return 0
    else:
        position += 1
        return 1 + count_sub_string_match_recursive(target[position:], key)


def test_count_sub_string():
    """testing our functions"""
    target1 = 'atgacatgcacaagtatgcat'
    target2 = 'atgaatgcatggatgtaaatgcag'
    key10 = 'a'
    key11 = 'atg'
    key12 = 'atgc'
    key13 = 'atgca'
    # Testing iterative version
    print "Iterative function"
    print count_sub_string_match(target1, key10)
    print count_sub_string_match(target1, key11)
    print count_sub_string_match(target1, key12)
    print count_sub_string_match(target1, key13)
    print count_sub_string_match(target2, key10)
    print count_sub_string_match(target2, key11)
    print count_sub_string_match(target2, key12)
    print count_sub_string_match(target2, key13)
    # Testing recursive version
    print "Recursive function"
    print count_sub_string_match_recursive(target1, key10)
    print count_sub_string_match_recursive(target1, key11)
    print count_sub_string_match_recursive(target1, key12)
    print count_sub_string_match_recursive(target1, key13)
    print count_sub_string_match_recursive(target2, key10)
    print count_sub_string_match_recursive(target2, key11)
    print count_sub_string_match_recursive(target2, key12)
    print count_sub_string_match_recursive(target2, key13)

test_count_sub_string()
