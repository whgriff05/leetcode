def wordPattern(pattern, s):
    cipherkey = {}
    s = s.split()
    if len(pattern) != len(s):
        return False
    
    for i in range(len(s)):
        if pattern[i] not in cipherkey and s[i] not in list(cipherkey.values()):
            cipherkey[pattern[i]] = s[i]
        if pattern[i] not in cipherkey and s[i] in list(cipherkey.values()):
            return False
        else:
            if s[i] != cipherkey[pattern[i]]:
                return False

    return True
            
    


# Tests
from testsuite import lc_test
lc_test(1, wordPattern("abba", "dog cat cat dog"), True)
lc_test(2, wordPattern("abba", "dog cat cat fish"), False)
lc_test(3, wordPattern("aaaa", "dog cat cat dog"), False)
