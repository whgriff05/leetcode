def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            #left sorted portion
            if nums[mid] < target or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
    
        else:
            # right sorted portion
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1 
    
            


# Tests
from testsuite import lc_test
lc_test(1, search([4, 5, 6, 7, 0, 1, 2], 0), 4)
lc_test(2, search([4, 5, 6, 7, 0, 1, 2], 3), -1)
lc_test(3, search([1], 0), -1)
lc_test(4, search([1, 3], 2), -1)
lc_test(5, search([5, 1, 3], 5), 0)
