def subarraySum(nums, k):
    running_sum = 0
    freqs = {0: 1} # Subarray with sum 0 already happens once (empty)
    ans = 0

    for n in nums:
        running_sum += n
        if running_sum - k in freqs:
            ans += freqs[running_sum - k]
        freqs[running_sum] = freqs.get(running_sum, 0) + 1

    return ans



# Tests
from testsuite import lc_test

lc_test(1, subarraySum([1, 1, 1], 2), 2)
lc_test(2, subarraySum([1, 2, 3], 3), 2)
lc_test(3, subarraySum([1], 0), 0)
