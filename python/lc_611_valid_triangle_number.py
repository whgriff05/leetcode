def triangleNumber(nums):
    n = len(nums)
    if n < 3:
        return 0

    nums.sort()
    count = 0

    for i in range(n-1, 1, -1):
        l, r = 0, i-1
        while l < r:
            if nums[l] + nums[r] > nums[i]:
                count += r - l
                r -= 1
            else:
                l += 1

    return count
                
        

def NAIVEtriangleNumber(nums):
    count = 0

    for s1 in range(0, len(nums) - 2):
        for s2 in range(s1+1, len(nums) - 1):
            for s3 in range(s2+1, len(nums)):
                    sides = [nums[s1], nums[s2], nums[s3]]
                    hyp = max(sides)
                    sides.remove(hyp)
                    if sum(sides) > hyp:
                        count += 1

    return count


# Tests
from testsuite import lc_test
lc_test(1, triangleNumber([2, 2, 3, 4]), 3)
lc_test(2, triangleNumber([4, 2, 3, 4]), 4)
