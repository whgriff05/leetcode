def missingNumber(nums):
    nums.sort()
    if nums[0] != 0:
        return 0
    for i in range(len(nums) - 1):
        if nums[i + 1] != (nums[i] + 1):
            return nums[i] + 1

    return max(nums) + 1
    

    
    


# Tests
from testsuite import lc_test
lc_test(1, missingNumber([3, 0, 1]), 2)
lc_test(2, missingNumber([0, 1]), 2)
lc_test(3, missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
