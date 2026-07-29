def permute(nums):
    results = []

    def backtrack(current_path):
        if len(current_path) == len(nums):
            results.append(list(current_path))
            return

        for n in nums:
            if n in set(current_path): continue
            current_path.append(n)
            backtrack(current_path)
            current_path.pop()


    backtrack([])
    return results

# Tests
from testsuite import lc_test

lc_test(1, permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

lc_test(2, permute([1, 2]), [[1, 2], [2, 1]])

lc_test(3, permute([1]), [[1]])

