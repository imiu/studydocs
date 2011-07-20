def fill_numbers(num_cnt, inc = 1):
    """docstring for fill_numbers"""
    i = 0
    numbers = []
    while i < num_cnt:
        print "At the top i is %d" %i
        numbers.append(i)

        i = i + inc
        print "Numbers now: " , numbers
        print "At the bottom i is %d" % i
    return numbers

numbers = fill_numbers(8, 2)

print "The numbers are:"
for num in numbers:
    print num

