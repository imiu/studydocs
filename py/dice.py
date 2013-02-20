#!/usr/bin/env python
from random import randrange
from operator import itemgetter


def roll(limit):
    value = 0
    while value < limit:
        yield randrange(1, 6)
        value += 1


def roll_analizer(roll_stats):
    sides = dict.fromkeys([1, 2, 3, 4, 5, 6], 0)
    tmp_sides = dict.fromkeys([1, 2, 3, 4, 5, 6], 0)
    prev = None
    for roll in roll_stats:
        tmp_sides[roll] += 1
        if prev is not None and prev != roll:
            if sides[prev] < tmp_sides[prev]:
                sides[prev] = tmp_sides[prev]
            tmp_sides[prev] = 0

        prev = roll
    if sides[roll] < tmp_sides[roll]:
        sides[roll] = tmp_sides[roll]

    return max(sides.iteritems(), key=itemgetter(1))


def test_roll_analyzer():
    stats = [1]
    result = (1, 1)
    print roll_analizer(stats) == result

    stats = [1, 1, 1]
    result = (1, 3)
    print roll_analizer(stats) == result

    stats = [1, 2, 2, 3, 2, 3]
    result = (2, 2)
    print roll_analizer(stats) == result

    stats = [1, 2, 2, 3, 2, 3, 3, 3]
    result = (3, 3)
    print roll_analizer(stats) == result


if __name__ == '__main__':
    test_roll_analyzer()
    from utils import bits
    bits(111)
