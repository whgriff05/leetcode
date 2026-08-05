import math

def shortestToChar(s, c):
    def initPointer(start):
        start += 1
        while start < len(s) and s[start] != c:
            start += 1
        if start >= len(s):
            return math.inf
        return start
        
    l = initPointer(-1)
    r = initPointer(l)

    output = []

    for i in range(len(s)):
        ldist = abs(l - i)
        rdist = abs(r - i)
        shortest = min(ldist, rdist)
        output.append(shortest)

        if i == r and i != 0:
            l = r
            r = initPointer(l)

    return output



# Tests
from testsuite import lc_test
lc_test(1, shortestToChar("loveleetcode", "e"), [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
lc_test(2, shortestToChar("aaab", "b"), [3, 2, 1, 0])
lc_test(2, shortestToChar("baaa", "b"), [0, 1, 2, 3])

