def twoSum(nums, target):
    nums_map = {}

    for i, x in enumerate(nums):
        nums_map[x] = nums_map.get(x, []) + [i]

    for x, indices in nums_map.items():
        val = target - x

        if val not in nums_map.keys(): # val does not exist
            continue

        if x == val and len(nums_map[val]) == 1: # val wants itself
            continue

        if x == val and len(nums_map[val]) > 1:
            return nums_map[val][0:2]

        return [nums_map[x][0], nums_map[val][0]]

# Tests


from testsuite import lc_test
lc_test(1, twoSum([2, 7, 11, 15], 9), [0, 1])
lc_test(2, twoSum([3, 2, 4], 6), [1, 2])
lc_test(3, twoSum([3, 3], 6), [0, 1])
