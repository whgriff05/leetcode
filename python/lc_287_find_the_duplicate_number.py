def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# Tests
from testsuite import lc_test
lc_test(1, findDuplicate([1, 3, 4, 2, 2]), 2)
lc_test(2, findDuplicate([3, 1, 3, 4, 2]), 3)
lc_test(3, findDuplicate([3, 3, 3, 3, 3]), 3)
