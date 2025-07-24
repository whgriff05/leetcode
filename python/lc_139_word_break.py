def wordBreak(s, wordDict):
    can_break = [False] * (len(s) + 1)
    can_break[0] = True

    for i in range(1, len(s) + 1):
        can_break[i] = any(can_break[j] and s[j:i] in wordDict for j in range(i))

    return can_break[len(s)]

# Tests
from testsuite import lc_test
lc_test(1, wordBreak("leetcode", ["leet", "code"]), True)
lc_test(2, wordBreak("applepenapple", ["apple", "pen"]), True)
lc_test(3, wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)
lc_test(4, wordBreak("aaaaaaa", ["aaaa", "aaa"]), True)
