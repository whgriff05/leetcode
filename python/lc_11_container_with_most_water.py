def maxArea(height):
    left = 0
    right = len(height) - 1

    max_vol = 0

    while left < right:
        tv = min(height[left], height[right]) * (right - left)
        if tv > max_vol:
            max_vol = tv

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_vol


# Tests
from testsuite import lc_test
lc_test(1, maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
lc_test(2, maxArea([1, 1]), 1)
