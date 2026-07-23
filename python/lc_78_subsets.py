def subsets(nums):
    key = (1 << len(nums)) - 1 

    output = []
    while key >= 0:
        skey = f"{key:0{len(nums)}b}"
        output.append([x for i, x in enumerate(nums) if skey[i] == "1"]) 
        key -= 1

    return output


# Tests
from testsuite import lc_test
lc_test(1, subsets([1, 2, 3]), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
"""
1 1 1
1 1 0
1 0 1
1 0 0
0 1 1
0 1 0
0 0 1
0 0 0

"""


lc_test(2, subsets([0]), [[], [0]])
