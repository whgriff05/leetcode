def permuteUnique(nums):
    results = []
    nums.sort() # bring duplicates together
    visited = [False] * len(nums)

    def backtrack(current_path):
        if len(current_path) == len(nums):
            results.append(list(current_path))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue

            visited[i] = True
            current_path.append(nums[i])
            backtrack(current_path)
            current_path.pop()
            visited[i] = False

    backtrack([])
    return results




def MYpermuteUnique(nums):
    results = []

    def backtrack(current_path):
        if len(current_path) == len(nums):
            l = list(map(lambda x: nums[x], current_path))
            if l not in results:
                results.append(l)
            return

        for n in range(len(nums)):
            if n in current_path: continue
            current_path.append(n)
            backtrack(current_path)
            current_path.pop()


    backtrack([])
    return results


# Tests
from testsuite import lc_test

lc_test(1, permuteUnique([1, 1, 2]), [[1, 1, 2], [1, 2, 1], [2, 1, 1]], sort_lists=False)
lc_test(2, permuteUnique([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], sort_lists=False)
