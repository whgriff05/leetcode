def lengthOfLongestSubstring(s):
    max_length = left = 0
    counts = {}

    for right, c in enumerate(s):
        counts[c] = counts.get(c, 0) + 1
        while counts[c] > 1:
            counts[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


def SETlengthOfLongestSubstring(s):
    left = max_length = 0
    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, len(char_set))

    return max_length

def COUNTSlengthOfLongestSubstring(s):
    if len(s) == 0: return 0
    maxc = 1
    l = 0
    counts = {s[l]: 1}

    for r in range(1, len(s)):
        counts[s[r]] = counts.get(s[r], 0) + 1

        if all(v == 1 for v in counts.values()):
            maxc = max(sum(counts.values()), maxc)
        else:
            counts[s[l]] -= 1
            if counts[s[l]] == 0:
                del counts[s[l]]
            l += 1

        

    return maxc


# Tests
from testsuite import lc_test

lc_test(1, lengthOfLongestSubstring("abcabcbb"), 3)
lc_test(2, lengthOfLongestSubstring("bbbbb"), 1)
lc_test(3, lengthOfLongestSubstring("pwwkew"), 3)
