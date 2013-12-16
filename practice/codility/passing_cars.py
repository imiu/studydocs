def prefix_sum(A):
    n = len(A)
    p = [0] * (n + 1)
    for k in xrange(1, n + 1):
        p[k] = p[k - 1] + A[k - 1]
    return p


def suffix_sum(A):
    n = len(A)
    s = [0] * (n + 1)
    ps = prefix_sum(A)
    ts = sum(A)
    for k in xrange(0, n + 1):
        s[k] = ts - ps[k]
    return s


def solution(A):
    # write your code in Python 2.6
    passing_cnt = 0
    total_cnt = 0
    for elm in reversed(A):
        if elm == 1:
            passing_cnt += 1
        else:
            total_cnt += passing_cnt
        if total_cnt > 1000000000:
            return -1
    return total_cnt

print solution([0, 1, 0, 1, 1])
