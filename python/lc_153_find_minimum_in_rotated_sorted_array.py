def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > 0 and nums[mid] < nums[mid-1]:
            return nums[mid]

        if left == right:
            return nums[right]

        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left]
        


# Tests
from testsuite import lc_test
lc_test(1, findMin([3, 4, 5, 1, 2]), 1)
lc_test(2, findMin([4, 5, 6, 7, 0, 1, 2]), 0)
lc_test(3, findMin([11, 13, 15, 17]), 11)
lc_test(4, findMin([3, 1, 2]), 1)
