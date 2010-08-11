from string import *


def count_sub_string_match_exact(target, key):
    """Find all occurrences of a string in another"""
    position_list = []
    position = 0
    pointer = 0
    while(pointer < len(target)):
        position = find(target, key, pointer)
        if position != -1:
            position_list.append(position)
            pointer = position + 1
        else:
            pointer += 1
    return tuple(position_list)


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
    print count_sub_string_match_exact(target1, key10)
    print count_sub_string_match_exact(target1, key11)
    print count_sub_string_match_exact(target1, key12)
    print count_sub_string_match_exact(target1, key13)
    print count_sub_string_match_exact(target2, key10)
    print count_sub_string_match_exact(target2, key11)
    print count_sub_string_match_exact(target2, key12)
    print count_sub_string_match_exact(target2, key13)

test_count_sub_string()
