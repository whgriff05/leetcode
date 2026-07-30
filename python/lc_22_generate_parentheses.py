def generateParenthesis(n):
    results = []

    def backtrack(current_string, open_count, close_count):
        if len(current_string) == 2*n:
            results.append(current_string)
            return

        if open_count < n:
            backtrack(f"{current_string}(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(f"{current_string})", open_count, close_count + 1)

    backtrack("", 0, 0)
    return results





# Tests
from testsuite import lc_test

lc_test(1, generateParenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
lc_test(2, generateParenthesis(1), ["()"])
