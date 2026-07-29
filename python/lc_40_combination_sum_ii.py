def combinationSum2(candidates, target):
    results = []
    candidates.sort()
    def backtrack(start_index, current_path, remaining_target):
        if remaining_target == 0:
            results.append(list(current_path))
            return
            
        for i in range(start_index, len(candidates)):
            if candidates[i] > remaining_target:
                break
                
            if i > start_index and candidates[i] == candidates[i-1]:
                continue
                
            current_path.append(candidates[i])
            backtrack(i + 1, current_path, remaining_target - candidates[i])
            current_path.pop()

    backtrack(0, [], target)
    return results

def tcombinationSum2(candidates, target):
    results = [] 
    candidates.sort()
    visited = [False] * len(candidates)

    def backtrack(current_path, target):
        if sum(current_path) == target:
            results.append(list(current_path))
            return

        for i in range(len(candidates)):
            if visited[i]:
                continue

            if i > 0 and candidates[i] == candidates[i-1] and candidates[i-1] and not visited[i-1]:
                continue

            visited[i] = True
            current_path.append(candidates[i])
            backtrack(current_path, target)
            current_path.pop()
            visited[i] = False


    backtrack([], target)
    return results



# Tests
from testsuite import lc_test

lc_test(1, combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])

lc_test(2, combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
