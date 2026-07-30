import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)


    def add(self, val): 
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]




# Tests
from testsuite import lc_test

kth = KthLargest(3, [4, 5, 8, 2])
lc_test(1, kth.add(3), 4)
lc_test(2, kth.add(5), 5)
lc_test(3, kth.add(10), 5)
lc_test(4, kth.add(9), 8)
lc_test(5, kth.add(4), 8)

kth = KthLargest(4, [7, 7, 7, 7, 8, 3])
lc_test(6, kth.add(2), 7)
lc_test(7, kth.add(10), 7)
lc_test(8, kth.add(9), 7)
lc_test(9, kth.add(9), 8)
