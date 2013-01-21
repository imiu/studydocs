#!/usr/bin/env python
# Graph representation
## Adjecency lists
a, b, c, d, e, f, g, h = range(8)
### Graph as a list of sets
Nls = [
    {b, c, d, e, f},    # a
    {c, e},             # b
    {d},                # c
    {e},                # d
    {f},                # e
    {c, g, h},          # f
    {f, h},             # g
    {f, g}              # h
]

### Graph as a list of lists, membership check is O(n)
Nll = [
    [b, c, d, e, f],    # a
    [c, e],             # b
    [d],                # c
    [e],                # d
    [f],                # e
    [c, g, h],          # f
    [f, h],             # g
    [f, g]              # h
]

### Graph as a list od dicts, with weights
Nld = [
    {b: 2, c: 1, d: 3, e: 9, f: 4},  # a
    {c: 4, e: 3},                    # b
    {d: 8},                          # c
    {e: 7},                          # d
    {f: 5},                          # e
    {c: 2, g: 2, h: 2},              # f
    {f: 1, h: 6},                    # g
    {f: 9, g: 8}                     # h
]

### Graph as a dict of sets
Nds = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}


## Adjecency matrix
Na = [[0, 1, 1, 1, 1, 1, 0, 0],  # a
      [0, 0, 1, 0, 1, 0, 0, 0],  # b
      [0, 0, 0, 1, 0, 0, 0, 0],  # c
      [0, 0, 0, 0, 1, 0, 0, 0],  # d
      [0, 0, 0, 0, 0, 1, 0, 0],  # e
      [0, 0, 1, 0, 0, 0, 1, 1],  # f
      [0, 0, 0, 0, 0, 1, 0, 1],  # g
      [0, 0, 0, 0, 0, 1, 1, 0]]  # h
if Na[a][b]:
    print "Is a neighbour"
print sum(Na[a]), " siblings"

_ = float('inf')
Naw = [[0, 2, 1, 3, 9, 4, _, _],  # a
       [_, 0, 4, _, 3, _, _, _],  # b
       [_, _, 0, 8, _, _, _, _],  # c
       [_, _, _, 0, 7, _, _, _],  # d
       [_, _, _, _, 0, 5, _, _],  # e
       [_, _, 2, _, _, 0, 2, 2],  # f
       [_, _, _, _, _, 1, 0, 6],  # g
       [_, _, _, _, _, 9, 8, 0]]  # h
if Naw[a][b] < _:
    print "Is a neighbour"
print sum(1 for w in Naw[a] if w < _) - 1, " siblpngs"

# It's even easier with numpy
import numpy as np
Nz = np.zeros([10, 10])
print Nz
