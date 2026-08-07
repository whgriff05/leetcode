def numberOfSubarrays(nums, k):
    # Turn array into 0 for even, 1 for odd
    for i in range(len(nums)):
        nums[i] %= 2

    pc = [0] * (len(nums) + 1) # "hash table" (index is key) of frequency
    pc[0] = 1
    s = 0
    total = 0

    for num in nums:
        s += num # Add to sum
        if s >= k: # If sum (count of odds) is ge k
            total += pc[s - k]
            # current prefix sum s - target previous prefix sum = k
            # therefore target previous prefix sum = s - k
            # we want frequency at target previous
        pc[s] += 1 # Increase frequency of sum

    return total

# Tests
from testsuite import lc_test

lc_test(1, numberOfSubarrays([1, 1, 2, 1, 1], 3), 2)

lc_test(2, numberOfSubarrays([2, 4, 6], 1), 0)

lc_test(3, numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2), 16)
