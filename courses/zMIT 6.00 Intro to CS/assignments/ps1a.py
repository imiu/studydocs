step = 2
current_int = 1
prime_cnt = 0
#def is_prime(int):
#    if int <= 1:
#        return False
#    for test in range(2, int):
#        if int % test == 0: return False;
#    return True

while prime_cnt < 1000:
    
    is_prime = True
    test_int = 2
    while test_int**2 <= current_int:
        if current_int % test_int == 0:
            is_prime = False
            break
        else:
            is_prime = True
        test_int += 1

    if is_prime:
        prime_cnt += + 1
        print prime_cnt, ' ', current_int    
     
    current_int = current_int + step

def some():
    do_some
    and_some
    and_more

def more():
    do_more
    and_more
    and_more_more


