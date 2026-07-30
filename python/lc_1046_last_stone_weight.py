import heapq

def lastStoneWeight(stones):
    stones = [-s for s in stones]
    
    heapq.heapify(stones)

    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)

        if x == y:
            continue

        y -= x
        heapq.heappush(stones, -y)

    if len(stones) == 1:
        return -stones[0]
    else:
        return 0





# Tests
from testsuite import lc_test

lc_test(1, lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)
lc_test(2, lastStoneWeight([1]), 1)
