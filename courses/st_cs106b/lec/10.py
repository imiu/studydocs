def rec_permutate(str, rem):
    if rem:
        for (idx, let) in enumerate(rem):
            rec_permutate(str + let, rem[0:idx] + rem[idx + 1:])
    else:
        print str


def mutate_wrapper(str):
    rec_permutate('', str)

# mutate_wrapper('abc')


def rec_subsets(str, rem):
    if rem:
        rec_subsets(str + rem[0], rem[1:])
        rec_subsets(str, rem[1:])
    else:
        print str


def subset_wrapper(str):
    rec_subsets('', str)


subset_wrapper('abc')
