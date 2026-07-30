def partition(s):
    results = []

    def backtrack(current_palindromes, start_index, end_index):
        if start_index == len(s):
            results.append(list(current_palindromes))
            return

        if end_index > len(s):
            return

        rev = "".join(reversed(s[start_index:end_index]))

        if s[start_index:end_index] == rev:
            current_palindromes.append(s[start_index:end_index])
            backtrack(current_palindromes, end_index, end_index + 1)
            current_palindromes.pop()

        backtrack(current_palindromes, start_index, end_index + 1)

    backtrack([], 0, 1)
    return results

        



# Tests
from testsuite import lc_test

lc_test(1, partition("aab"), [["a", "a", "b"], ["aa", 'b']])

lc_test(2, partition("a"), [["a"]])
