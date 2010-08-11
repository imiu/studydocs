###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0           # variable that keeps track of largest number
packages = (3,14,17)     # variable that contains package sizes

max_n = 150
max_values = (max_n/packages[0] +1, max_n/packages[1] + 1, max_n/packages[2] + 1)

n_tuple = ()
for n in range(1, max_n):   # only search for solutions up to size 150
    for a in range(0, max_values[0]):
        for b in range(0, max_values[0]):
            for c in range(0, max_values[0]):
                eq = packages[0] * a + packages[1] * b + packages[2] * c
                if eq == n:
                    is_unique = True
                    for tmp_n in n_tuple:
                        if tmp_n == n:
                            is_unique = False
                    if is_unique:
                        n_tuple += (n,)

print n_tuple
maximum = 0
for max_n in range(1, n):
    if max_n not in n_tuple:
        bestSoFar = max_n
        
print 'Given package sizes', packages[0], ',', packages[1], 'and', packages[2], ' the largest number of McNuggets that cannot be bought in exact quantity is: ', bestSoFar