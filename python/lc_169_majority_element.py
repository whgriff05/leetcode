def majorityElement(nums):
    nd = {}
    for num in nums:
        if num in nd:
            nd[num] += 1
        else:
            nd[num] = 1

    maj = list(nd.keys)[0]
    for num in nd.keys():
        if nd[num] > nd[maj]:
            maj = num

    return maj
    


# Tests
from testsuite import lc_test
lc_test(1, majorityElement([3, 2, 3]), 3)
lc_test(2, majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
