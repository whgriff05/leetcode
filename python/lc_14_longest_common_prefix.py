def longestCommonPrefix(strs):
    prefix = ""
    if len(strs[0]) == 0:
        return prefix

    in_common = True
    while in_common:
        if len(strs[0]) == len(prefix):
            in_common = False
            break
        common_letter = strs[0][len(prefix)]
        for word in strs:
            if len(word) == len(prefix):
                in_common = False
                break
            if word[len(prefix)] != common_letter:
                in_common = False
                break
        if in_common:
            prefix += common_letter

    return prefix



# Tests
from testsuite import lc_test
lc_test(1, longestCommonPrefix(["flower", "flow", "flight"]), "fl")
lc_test(2, longestCommonPrefix(["dog", "racecar", "car"]), "")
