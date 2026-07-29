def letterCombinations(digits):
    results = []
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    } 

    def backtrack(i, current_str):
        if len(current_str) == len(digits):
            results.append(str(current_str))
            return

        if i >= len(digits):
            return

        for j in range(len(mapping[digits[i]])):
            cs = f"{current_str}{mapping[digits[i]][j]}"
            backtrack(i+1, cs)

    backtrack(0, "")

    return results

        


# Tests
from testsuite import lc_test

lc_test(1, letterCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
lc_test(2, letterCombinations("2"), ["a", "b", "c"])
