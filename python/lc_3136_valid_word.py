def isValid(word):
    has_vowel = False
    has_consonant = False
    is_alphanum = True

    for char in word:
        if char.lower() in "aeiou":
            has_vowel = True
        elif char.lower() in "bcdfghjklmnpqrstvwxyz":
            has_consonant = True
        elif char not in "1234567890":
            is_alphanum = False

    return has_vowel and has_consonant and is_alphanum and (len(word) >= 3)


# Tests
from testsuite import lc_test
lc_test(1, isValid("234Adas"), True)
lc_test(2, isValid("b3"), False)
lc_test(3, isValid("a3$e"), False)
