def isPowerOfThree(n):
    t = 1
    
    while t < n:
        t *= 3

    if t == n:
        return True
    return False



# Tests
from testsuite import lc_test
lc_test(1, isPowerOfThree(27), True)
lc_test(2, isPowerOfThree(0), False)
lc_test(3, isPowerOfThree(-1), False)
