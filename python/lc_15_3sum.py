def threeSum(nums):
    output = []
    nums.sort()

    for index, value in enumerate(nums):
        if index > 0 and value == nums[index-1]:
            continue

        l = index + 1
        r = len(nums) - 1
        while l < r:
            three = value + nums[l] + nums[r]
            if three > 0:
                r -= 1
            elif three < 0:
                l += 1
            else:
                output.append([value, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
        

    return output

# Tests


from testsuite import lc_test
lc_test(1, threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
lc_test(2, threeSum([0, 1, 1]), [])
lc_test(3, threeSum([0, 0, 0]), [[0, 0, 0]])
