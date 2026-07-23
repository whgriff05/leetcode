def singleNumber(nums):
    result = 0

    for i in range(32):
        bit_count = sum((num >> i) & 1 for num in nums)
        if bit_count % 3:
            if i == 31:
                result -= (1 << i) # a negative number (last bit is sign bit)
            else:
                result |= (1 << i) # other information bits
    
    return result


# Tests
from testsuite import lc_test
lc_test(1, singleNumber([2, 2, 3, 2]), 3)
lc_test(2, singleNumber([0, 1, 0, 1, 0, 1, 99]), 99)
