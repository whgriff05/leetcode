def findAnagrams(s, p):
    ana = {}
    window = {}

    for c in p:
        ana[c] = ana.get(c, 0) + 1

    for c in s[:len(p)]:
        window[c] = window.get(c, 0) + 1

    left = 0
    ans = []

    if window == ana:
        ans.append(left)

    for right in range(len(p), len(s)):
        window[s[right]] = window.get(s[right], 0) + 1

        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]

        left += 1

        if ana == window:
            ans.append(left)

    return ans



# Tests

from testsuite import lc_test

lc_test(1, findAnagrams("cbaebabacd", "abc"), [0, 6])
lc_test(2, findAnagrams("abab", "ab"), [0, 1, 2])
