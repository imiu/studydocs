def solution(A):
    # write your code in Python 2.6
    min_value = A[0]
    max_profit = 0
    for elm in A:
        if elm < min_value:
            min_value = elm
        else:
            if elm - min_value > max_profit:
                max_profit = elm - min_value

    return max_profit


print solution([23171, 21015, 21123, 21366, 21013, 21367])
