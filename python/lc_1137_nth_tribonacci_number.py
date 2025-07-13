def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    
    t0 = 0
    t1 = 1
    t2 = 1
    for i in range(n - 2):
        s = t0 + t1 + t2
        t0 = t1
        t1 = t2
        t2 = s

    return t2


# Tests
from testsuite import lc_test
lc_test(1, tribonacci(4), 4)
lc_test(2, tribonacci(25), 1389537)
