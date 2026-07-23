def subsets(nums):
    key = (1 << len(nums)) - 1 

    output = []
    while key >= 0:
        skey = f"{key:0{len(nums)}b}"
        output.append(tuple(sorted(x for i, x in enumerate(nums) if skey[i] == "1")))
        key -= 1

    output = set(output)
    return [[x for x in tup] for tup in output]


# Tests
from testsuite import lc_test
lc_test(1, subsets([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
lc_test(2, subsets([0]), [[], [0]])
