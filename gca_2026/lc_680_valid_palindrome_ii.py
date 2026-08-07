def validPalindrome(s):
    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return is_palindrome(l, r-1) or is_palindrome(l+1, r)
        l += 1
        r -= 1

    return True



# Tests
from testsuite import lc_test

lc_test(1, validPalindrome("aba"), True)
lc_test(2, validPalindrome("abca"), True)
lc_test(3, validPalindrome("abc"), False)
