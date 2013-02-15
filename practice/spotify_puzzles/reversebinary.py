#!/usr/bin/env python
if __name__ == '__main__':
    raw_int = raw_input()
    print int(''.join(reversed(bin(int(raw_int))[2:])), 2)
