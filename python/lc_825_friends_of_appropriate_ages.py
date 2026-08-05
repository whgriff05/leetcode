from collections import Counter

def numFriendRequests(ages):
    count = 0
    ages = Counter(ages)
    for x in ages:
        x_count = ages[x]
        for y in ages:
            if not (y <= 0.5 * x + 7 or y > x):
                y_count = ages[y]
                if x != y:
                    count += x_count * y_count
                else:
                    count += x_count * (x_count - 1)

    return count
                

# Tests
from testsuite import lc_test
lc_test(1, numFriendRequests([16, 16]), 2)
lc_test(2, numFriendRequests([16, 17, 18]), 2)
lc_test(3, numFriendRequests([20, 30, 100, 110, 120]), 3)
lc_test(4, numFriendRequests([54,23,102,90,40,74,112,74,76,21]), 22)
