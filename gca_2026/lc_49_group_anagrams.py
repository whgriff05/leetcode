def groupAnagrams(strs):
    ana = {}

    for s in strs:
        k = "".join(sorted(s))
        ana[k] = ana.get(k, []) + [s]

    return list(ana.values())


# Tests
from testsuite import lc_test

lc_test(1, groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]], sort_lists=True)
