def removeDuplicates(nums):
    n = len(nums)
    i = 0
    in_nums = {}

    while i != n:
        if nums[i] not in in_nums:
            in_nums[nums[i]] = 1
            i += 1
        else:
            if in_nums[nums[i]] == 1:
                in_nums[nums[i]] += 1
                i += 1
            else:
                del nums[i]
                n -= 1

    
    return n

# Tests
from testsuite import lc_test
lc_test(1, removeDuplicates([1, 1, 1, 2, 2, 3]), 5)
lc_test(2, removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]), 7)


