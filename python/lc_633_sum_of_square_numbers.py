import math

def judgeSquareSum(c):
    l = 0
    r = int(math.sqrt(c))

    while l <= r:
        s = l**2 + r**2
        if s == c:
            return True
        elif s > c:
            r -= 1
        else:
            l += 1

    return False

    

def NAIVEjudgeSquareSum(c):
    size = int(math.sqrt(c)) + 3
    nums = [i**2 for i in range(size)]

    l, r = size - 1, size - 1
    while r >= 0:
        if l < 0:
            r -= 1
            l = r
            
        if nums[l] + nums[r] == c:
            return True
        elif nums[l] + nums[r] > c:
            l -= 1
        elif nums[l] + nums[r] < c:
            r -= 1
            l = r
    return False
            
        
    


# Tests
from testsuite import lc_test
lc_test(1, judgeSquareSum(5), True)
lc_test(1, judgeSquareSum(3), False)
