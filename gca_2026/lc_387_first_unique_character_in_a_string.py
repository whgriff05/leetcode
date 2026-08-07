import collections

def firstUniqChar(s):
    charcounts = dict(collections.Counter(s))

    for k in charcounts:
        if charcounts[k] == 1:
            return list(s).index(k)

    return -1

# Tests
from testsuite import lc_test

lc_test(1, firstUniqChar("leetcode"), 0)
lc_test(2, firstUniqChar("loveleetcode"), 2)
lc_test(3, firstUniqChar("aabb"), -1)
