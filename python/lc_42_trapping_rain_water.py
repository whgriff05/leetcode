def trap(height):
    count = 0
    left = 0

    while left < len(height) - 1:
        mid = left + 1
        curr = 0
        while height[mid] < height[left]:
            curr += height[left] - height[mid]
            mid += 1
            if mid >= len(height):
                curr = 0
                break

        count += curr
        left = mid

    right = len(height) - 1
    while right > 0:
        mid = right - 1
        curr = 0
        while height[mid] <= height[right]:
            curr += height[right] - height[mid]
            mid -= 1
            if mid < 0:
                curr = 0
                break

        count += curr
        right = mid

    return count
    

    


# Tests
from testsuite import lc_test
lc_test(1, trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
lc_test(2, trap([4,2,0,3,2,5]), 9)
lc_test(3, trap([4, 2, 3]), 1)
lc_test(4, trap([5,4,1,2]), 1)
