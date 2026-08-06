import collections

def longestPalindrome(words):
    pairs = []
    singles = []

    wd = dict(collections.Counter(words))

    for w in wd.keys():
        if w[::-1] == w and w not in pairs and w not in singles:
            if wd[w] % 2:
                for _ in range(wd[w] - 1): pairs.append(w)
                singles.append(w)
            else:
                for _ in range(wd[w]): pairs.append(w)

        else:
            if w[::-1] in wd.keys() and w not in pairs:
                for _ in range(min(wd[w], wd[w[::-1]])):
                    pairs.append(w)
                    pairs.append(w[::-1])
            

    return len(pairs) * 2 + (2 if len(singles) >= 1 else 0)

# Tests
from testsuite import lc_test

lc_test(1, longestPalindrome(["lc", "gg", "cl"]), 6)
lc_test(2, longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]), 8)
lc_test(3, longestPalindrome(["cc", "ll", "xx"]), 2)
lc_test(4, longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]), 22)
