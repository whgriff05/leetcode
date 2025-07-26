def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    d1 = {}
    d2 = {}
    for c in s1:
        if c in d1:
            d1[c] += 1
        else:
            d1[c] = 1

    for i in range(len(s1)):
        c = s2[i]
        if c in d2:
            d2[c] += 1
        else:
            d2[c] = 1

    l = 0
    r = 0

    for i in range(len(s2) - len(s1) + 1):
        l = i
        r = l + len(s1) - 1
        if i != 0:
            d2[s2[l-1]] -= 1
            if d2[s2[l-1]] == 0:
                del d2[s2[l-1]]
            if s2[r] in d2:
                d2[s2[r]] += 1
            else:
                d2[s2[r]] = 1

        if d1 == d2:
            return True

    return False

    
        


# Tests
from testsuite import lc_test
lc_test(1, checkInclusion("ab", "eidbaooo"), True)
lc_test(2, checkInclusion("ab", "eidboaoo"), False)
