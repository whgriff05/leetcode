import heapq

def findKthLargest(nums, k):
    return list(sorted(nums))[-(k)]

def HEAPfindKthLargest(nums, k):
    heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)

    return nums[0]


# Tests
from testsuite import lc_test

lc_test(1, findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
lc_test(2, findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

