def romanToInt(s):
    cipher = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            }

    total = 0
    
    pointer = 0
    while pointer < len(s):
        if pointer < len(s) - 1 and cipher[s[pointer]] < cipher[s[pointer + 1]]:
            total += cipher[s[pointer + 1]] - cipher[s[pointer]]
            pointer += 2
        else:
            total += cipher[s[pointer]]
            pointer += 1

    return total


# Tests
from testsuite import lc_test
lc_test(1, romanToInt("III"), 3)
lc_test(2, romanToInt("LVIII"), 58)
lc_test(3, romanToInt("MCMXCIV"), 1994)
