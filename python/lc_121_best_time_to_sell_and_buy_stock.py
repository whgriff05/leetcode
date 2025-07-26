def maxProfit(prices):
    ans = 0
    mi = max(prices)

    for v in prices:
        ans = max(v - mi, ans)
        mi = min(mi, v)

    return ans

# Tests
from testsuite import lc_test
lc_test(1, maxProfit([7,1,5,3,6,4]), 5)
lc_test(2, maxProfit([7,6,4,3,1]), 0)
