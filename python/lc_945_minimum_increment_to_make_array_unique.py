def minIncrementForUnique(nums):
    nums.sort()
    output = 0

    i = 1
    while i < len(nums):
        if nums[i] <= nums[i-1]:
            inc = nums[i-1] - nums[i] + 1
            output += inc
            nums[i] = nums[i-1] + 1

        i += 1

    return output

# Tests
from testsuite import lc_test

lc_test(1, minIncrementForUnique([1, 2, 2]), 1)
lc_test(2, minIncrementForUnique([3, 2, 1, 2, 1, 7]), 6)
