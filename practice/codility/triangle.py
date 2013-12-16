def solution(A):
    A.sort()
    prd_right = 1
    for elm in A[-3:]:
        prd_right *= elm

    prd_left = A[0] * A[1] * A[len(A) - 1]

    return max(prd_left, prd_right)

# print solution([10, 2, 5, 1, 8, 20])
print solution([10, 50, 5, 1])
