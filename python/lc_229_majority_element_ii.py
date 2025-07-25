def majorityElement(nums):
    nd = {}
    for num in nums:
        if num in nd:
            nd[num] += 1
        else:
            nd[num] = 1

    output = []
    for num in nd.keys():
        if nd[num] > len(nums)/3:
            output.append(num)

    return output
    


# Tests
from testsuite import lc_test
lc_test(1, majorityElement([3, 2, 3]), [3])
lc_test(2, majorityElement([1]), [1])
lc_test(3, majorityElement([1, 2]), [1, 2])
