def longestConsecutive(nums):
    if not nums:
        return 0
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    overall = 0
    nums_dict = dict(sorted(nums_dict.items()))
    k = 1
    nums = list(nums_dict.keys())
    for i in range(len(nums)-1):
        if nums[i] + 1 == nums[i+1]:
            k += 1
        else:
            overall = max(overall, k)
            k = 1

    overall = max(overall, k)
        
        
    return overall



# Tests
from testsuite import lc_test
lc_test(1, longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
lc_test(2, longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
lc_test(3, longestConsecutive([1, 0, 1, 2]), 3)
lc_test(4, longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]), 7)
