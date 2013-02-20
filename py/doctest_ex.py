#!/usr/bin/env python


def add_10(x):
    """
    adds 10 to the input value
    >>> add_10(5)
    15
    >>> add_10(-2)
    8
    """
    return x + 10

if __name__ == "__main__":
    import doctest
    doctest.testmod()
