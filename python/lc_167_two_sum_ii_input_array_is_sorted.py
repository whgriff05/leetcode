def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1


# Tests
from testsuite import lc_test
lc_test(1, twoSum([2, 7, 11, 15], 9), [1, 2])
lc_test(2, twoSum([2, 3, 4], 6), [1, 3])
lc_test(3, twoSum([-1, 0], -1), [1, 2])
