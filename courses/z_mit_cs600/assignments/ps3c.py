from string import *


def sub_string_match_exact(target, key):
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


def constrained_match_pair(first_match, second_match, length):
    """ Find intersection """
    intersection = []
    for n in first_match:
        for m in second_match:
            if n + length + 1 == m:
                intersection.append(n)
    return tuple(intersection)


def sub_string_match_one_sub(target, key):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0, len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key', key, 'into', key1, key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = sub_string_match_exact(target, key1)
        match2 = sub_string_match_exact(target, key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrained_match_pair(match1, match2, len(key1))
        allAnswers = allAnswers + filtered
        print 'match1', match1
        print 'match2', match2
        print 'possible matches for', key1, key2, 'start at', filtered
        print ''
    return allAnswers


def test_count_sub_string():
    """testing our functions"""
    target1 = 'atgacatgcacaagtatgcat'
    target2 = 'atgaatgcatggatgtaaatgcag'
    #key10 = 'a'
    key11 = 'atg'
    key12 = 'atgc'
    key13 = 'atgca'
    # Testing problem 3    
    # print sub_string_match_one_sub(target1, key10)
    print sub_string_match_one_sub(target1, key11)
    print sub_string_match_one_sub(target1, key12)
    print sub_string_match_one_sub(target1, key13)
    # print sub_string_match_one_sub(target2, key10)
    print sub_string_match_one_sub(target2, key11)
    print sub_string_match_one_sub(target2, key12)
    print sub_string_match_one_sub(target2, key13)

test_count_sub_string()
