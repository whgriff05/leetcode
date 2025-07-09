def longestPalindrome(s):
    length = 0
    char_dict = {}
    at_ready = False
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1



    for char in char_dict:
        if char_dict[char] >= 2:
            length += char_dict[char] // 2 * 2
            char_dict[char] -= char_dict[char] // 2 * 2
            if char_dict[char] == 1:
                at_ready = True
        elif char_dict[char] == 1: 
            at_ready = True

    if at_ready:
        length += 1

    return length

            
# Tests
from testsuite import lc_test
lc_test(1, longestPalindrome("abccccdd"), 7)
lc_test(2, longestPalindrome("a"), 1)
lc_test(3, longestPalindrome("bb"), 2)
