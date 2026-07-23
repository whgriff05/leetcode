def isPalindrome(x):
    if x < 0: return False
    if x < 10: return True

    ox = x
    y = 0

    while x != 0:
        y = y * 10 + (x % 10)
        x //= 10

    return y == ox

# Tests


from testsuite import lc_test
lc_test(1, isPalindrome(121), True)
lc_test(2, isPalindrome(-121), False)
lc_test(3, isPalindrome(10), False)
