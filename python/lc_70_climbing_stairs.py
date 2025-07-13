def climbStairs(n):
    p1 = 0
    p2 = 1
    for i in range(n):
        s = p1 + p2
        p1 = p2
        p2 = s
    return p2


"""
fib sequence: (0 1) 1 2 3 5 8 


2: 1,1 | 2
3: 1,1,1 | 2,1 | 1,2
4: 1,1,1,1 | 2,1,1 | 1,2,1 | 1,1,2 | 2,2
5: 1,1,1,1,1 | 2,1,1,1 | 1,2,1,1 | 1,1,2,1 | 1,1,1,2 | 2,2,1 | 2,1,2 | 1,2,2
"""

# Tests
from testsuite import lc_test
lc_test(1, climbStairs(2), 2)
lc_test(2, climbStairs(3), 3)
