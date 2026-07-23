def singleNumber(nums):
    key = 0

    for n in nums:
        key ^= n

    return key

# Tests
from testsuite import lc_test
lc_test(1, singleNumber([2, 2, 1]), 1)
lc_test(2, singleNumber([4, 1, 2, 1, 2]), 4)
lc_test(3, singleNumber([1]), 1)
lc_test(4, singleNumber([3, 1, 2, 1, 2]), 3)
