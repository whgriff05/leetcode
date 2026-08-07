def containsNearbyDuplicate(nums, k):
    numdiff = {}

    for i, n in enumerate(nums):
        if n not in numdiff:
            numdiff[n] = i
        else:
            if i - numdiff[n] <= k: return True
            else:
                numdiff[n] = i

    return False


def SLOWcontainsNearbyDuplicate(nums, k):
    numindices = {}

    for i, n in enumerate(nums):
        numindices[n] = numindices.get(n, []) + [i]

    for _, v in numindices.items():
        for i in range(1, len(v)):
            if v[i] - v[i-1] <= k:
                return True

    return False


# Tests
from testsuite import lc_test

lc_test(1, containsNearbyDuplicate([1, 2, 3, 1], 3), True)
lc_test(2, containsNearbyDuplicate([1, 0, 1, 1], 1), True)
lc_test(3, containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), False)

