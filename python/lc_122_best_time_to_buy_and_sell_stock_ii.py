def maxProfit(prices):
    mode = "buy"
    profit = 0

    i = 0
    while i < len(prices):
        if mode == "buy":
            if i+1 < len(prices) and prices[i] > prices[i+1]:
                i += 1
            elif i+1 < len(prices) and prices[i] <= prices[i+1]:
                profit -= prices[i]
                mode = "sell"
                i += 1
            else:
                i += 1
        elif mode == "sell":
            if i+1 < len(prices) and prices[i] < prices[i+1]:
                i += 1
            elif i+1 < len(prices) and prices[i] >= prices[i+1]:
                profit += prices[i]
                mode = "buy"
                i += 1
            else:
                profit += prices[i]
                mode = "buy"
                i += 1

    return profit
        

    

# Tests
from testsuite import lc_test
lc_test(1, maxProfit([7, 1, 5, 3, 6, 4]), 7)
lc_test(2, maxProfit([1, 2, 3, 4, 5]), 4)
lc_test(3, maxProfit([7, 6, 4, 3, 1]), 0)
