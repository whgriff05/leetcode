def combine(n, k):
    results = []
    candidates = list(range(1, n+1))

    def backtrack(i, current_path):
        if len(current_path) == k:
            results.append(list(current_path))
            return

        if i >= len(candidates):
            return

        current_path.append(candidates[i])
        backtrack(i+1, current_path)

        current_path.pop()
        backtrack(i+1, current_path)


    backtrack(0, [])
    return results


# Tests
from testsuite import lc_test
lc_test(1, combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
lc_test(2, combine(1, 1), [[1]])
