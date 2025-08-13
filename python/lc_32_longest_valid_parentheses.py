def longestValidParentheses(s):
    dp = [0] * (len(s) + 1)


    for index, char in enumerate(s, 1):
        if char == ')':
            if index > 1 and s[index - 2] == "(":
                dp[index] = dp[index - 2] + 2
            else:
                match_index = index - dp[index - 1] - 1
                if match_index > 0 and s[match_index - 1] == "(":
                    dp[index] = dp[index - 1] + 2 + dp[match_index - 1]

    return max(dp)
        


# Tests
from testsuite import lc_test
lc_test(1, longestValidParentheses("(()"), 2)
lc_test(2, longestValidParentheses(")()())"), 4)
lc_test(3, longestValidParentheses(""), 0)
lc_test(4, longestValidParentheses("()(())"), 6)
lc_test(5, longestValidParentheses("()(()"), 2)
lc_test(6, longestValidParentheses("(()(((()"), 2)
