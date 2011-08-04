def fib(n):
    """docstring for fib"""
    print 'n =', n
    if n > 1:
        return n * fib(n - 1)
    else:
        print "end of the line"
        return 1

print fib(5)
print fib(10)
print fib(15)
