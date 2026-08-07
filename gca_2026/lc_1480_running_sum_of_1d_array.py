def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]

    return nums


# Tests
from testsuite import lc_test

lc_test(1, runningSum([1, 2, 3, 4]), [1, 3, 6, 10])

lc_test(2, runningSum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])

lc_test(3, runningSum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])
