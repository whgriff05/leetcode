def longestPalindrome(s):
    res = ""
    res_len = 0

    for i in range(len(s)):
        l = i
        r = i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1

            l -= 1
            r += 1

        l = i
        r = i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1

            l -= 1
            r += 1

    return res
                
        
                


# Tests
from testsuite import lc_test

lc_test(1, longestPalindrome("babad"), "bab")
lc_test(2, longestPalindrome("cbbd"), "bb")
lc_test(3, longestPalindrome("ccc"), "ccc")
