def solution(N):
    bns = str(bin(N))[2:]
    running_cnt = 0
    max_cnt = 0
    for elm in bns:
        if elm == '0':
            running_cnt += 1
        else:
            if max_cnt < running_cnt:
                max_cnt = running_cnt
            running_cnt = 0
    return max_cnt
