def removeDuplicates(nums):
    n = len(nums)
    in_nums = []
    i = 0
    while i != n:
        if nums[i] not in in_nums:
            in_nums.append(nums[i])
            i += 1
        else:
            del nums[i]
            n -= 1

    return n

# Tests
from testsuite import lc_test
lc_test(1, removeDuplicates([1, 1, 2]), 2)
lc_test(2, removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)


