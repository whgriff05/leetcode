def combinationSum(candidates, target):
    results = []

    def backtrack(i, current_path, remaining_target):
        if remaining_target == 0:
            results.append(list(current_path))
            return

        if remaining_target < 0 or i >= len(candidates):
            return

        current_path.append(candidates[i])
        backtrack(i, current_path, remaining_target - candidates[i])

        current_path.pop()
        backtrack(i+1, current_path, remaining_target)

    backtrack(0, [], target)
    return results


            
           





# Tests
from testsuite import lc_test

lc_test(1, combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
lc_test(2, combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
