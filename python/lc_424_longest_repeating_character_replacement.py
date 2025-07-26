def characterReplacement(s, k):
    count = {}
    res = 0
    
    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res
    


# Tests
from testsuite import lc_test
lc_test(1, characterReplacement("ABAB", 2), 4)
lc_test(2, characterReplacement("AABABBA", 1), 4)
