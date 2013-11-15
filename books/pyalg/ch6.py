#! /usr/bin/env python
# -*- coding: utf-8


def skyline_n2(inp):
    max_elm = max(inp, key=lambda x: x[2])
    max_x = max_elm[2]
    skyline = [0] * (max_x + 1)
    for elm in inp:
        for s in range(elm[0], elm[2]):
            print s
            if skyline[s] < elm[1]:
                skyline[s] = elm[1]

    prev = 0
    result = []
    print skyline
    for x, y in enumerate(skyline):
        print x, y
        if y != prev:
            result.append((x, y))
            prev = y

    return result


def skylinize(b):
    return [(b[0][0], b[0][1]), (b[0][2], 0)]


def skymerge(sky1, sky2):
    sky = []
    curr_h1 = 0
    curr_h2 = 0
    prev = (0, 0)
    while sky1 and sky2:
        if sky1[0][0] < sky2[0][0]:
            elm = sky1.pop(0)
            curr_x = elm[0]
            curr_h1 = elm[1]
            if (prev[1] != max(curr_h1, curr_h2)):
                sky.append((curr_x, max(curr_h1, curr_h2)))
                prev = elm
        else:
            elm = sky2.pop(0)
            curr_x = elm[0]
            curr_h2 = elm[1]
            if (prev[1] != max(curr_h1, curr_h2)):
                sky.append((curr_x, max(curr_h1, curr_h2)))
                prev = elm
    if sky2 and not sky1:
        sky.extend(sky2)
    elif sky1 and not sky2:
        sky.extend(sky1)
    return sky


def skyline(inp):
    l = len(inp)
    if l == 1:
        sk = skylinize(inp)
        return sk
    hi, lo = skyline(inp[:l / 2]), skyline(inp[l / 2:])
    return skymerge(hi, lo)
