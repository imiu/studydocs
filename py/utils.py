def bits(n):
    n += 2**32
    return bin(n)[-32:]  # remove '0b'
