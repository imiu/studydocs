def solution(T):
    def tree_height(T):
        # write your code in Python 2.6
        if T is None:
            return 0
        return 1 + max(tree_height(T.r), tree_height(T.l))

    return tree_height(T) - 1
