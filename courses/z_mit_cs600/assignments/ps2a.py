a = 1
b = 1
c = 1
eq = 6 * a + 9 * b + 20 * c

n = 200

max_a = n / 6 + 1
max_b = n / 9 + 1
max_c = n / 20 + 1

n_tuple = ()
for n in range(1, n):
    for a in range(0, max_a):
        for b in range(0, max_b):
            for c in range(0, max_c):
                eq = 6 * a + 9 * b + 20 * c
                if eq == n:
                    print n
                    print 'We found it: a =', a, ',  b=', b, ', c=', c
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
        maximum = max_n
        
print 'Largest number of McNuggets that cannot be bought in exact quantity: ', maximum