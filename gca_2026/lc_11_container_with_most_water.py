def maxArea(height):
    l = 0
    r = len(height) - 1
    ma = 0

    while l < r:
        area = (r - l)  * min(height[l], height[r])
        if area > ma:
            ma = area
        
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return ma


# Tests
from testsuite import lc_test

lc_test(1, maxArea([1,8,6,2,5,4,8,3,7]), 49)
lc_test(2, maxArea([1, 1]), 1)
