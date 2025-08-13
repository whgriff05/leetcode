def search(nums, target):
    lowest_bound = 0
    highest_bound = len(nums) - 1
    if target > nums[-1] or target < nums[0]:
        return -1

    while lowest_bound != highest_bound:
        mp = len(nums[lowest_bound:highest_bound + 1]) // 2 + lowest_bound
        if nums[mp] > target:
            highest_bound = mp - 1
        elif nums[mp] < target:
            lowest_bound = mp + 1
        else:
            return mp

    if nums[lowest_bound] == target:
        return lowest_bound
    else:
        return -1

    

# Tests
from testsuite import lc_test
lc_test(1, search([-1, 0, 3, 5, 9, 12], 9), 4)
lc_test(2, search([-1, 0, 3, 5, 9, 12], 2), -1)
