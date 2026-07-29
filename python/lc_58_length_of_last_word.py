def lengthOfLastWord(s):
    return len(s.split()[-1])


# Tests
from testsuite import lc_test

lc_test(1, lengthOfLastWord("Hello World"), 5)
lc_test(2, lengthOfLastWord("   fly   me  to the    moon"), 4)
lc_test(3, lengthOfLastWord("luffy is still joyboy"), 6)
