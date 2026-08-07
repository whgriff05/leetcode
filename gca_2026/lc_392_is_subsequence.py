def isSubsequence(s, t):
    i = 0
    j = 0

    while j < len(t) and i < len(s):
        if s[i] != t[j]:
            j += 1
        else:
            i += 1
            j += 1

    if i == len(s):
        return True
    return False



# Tests
from testsuite import lc_test

lc_test(1, isSubsequence("abc", "ahbgdc"), True)
lc_test(2, isSubsequence("axc", "ahbgdc"), False)
lc_test(3, isSubsequence("b", "abc"), True)
lc_test(4, isSubsequence("", "abc"), True)

