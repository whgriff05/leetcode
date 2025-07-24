def lengthOfLongestSubstring(s):
    starting_pos = 0
    current_pos = 0
    current_letters = []
    max_count = 0
    while starting_pos < len(s) and current_pos < len(s):
        if s[current_pos] in current_letters:
            starting_pos += 1
            current_pos = starting_pos
            max_count = max(len(current_letters), max_count)
            current_letters = []
        elif s[current_pos] not in current_letters:
            current_letters.append(s[current_pos])
            current_pos += 1

    return max(max_count, len(current_letters))


# Tests
from testsuite import lc_test
lc_test(1, lengthOfLongestSubstring("abcabcbb"), 3)
lc_test(2, lengthOfLongestSubstring("bbbbb"), 1)
lc_test(3, lengthOfLongestSubstring("pwwkew"), 3)
lc_test(4, lengthOfLongestSubstring(" "), 1)
