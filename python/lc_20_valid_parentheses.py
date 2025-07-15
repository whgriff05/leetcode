def isValid(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if len(stack) == 0:
                return False
            opening_char = stack.pop()
            if opening_char == "(" and char != ")":
                return False
            elif opening_char == "{" and char != "}":
                return False
            elif opening_char == "[" and char != "]":
                return False

    if len(stack) != 0:
        return False

    return True

            
# Tests
from testsuite import lc_test
lc_test(1, isValid("()"), True)
lc_test(2, isValid("()[]{}"), True)
lc_test(3, isValid("(]"), False)
lc_test(4, isValid("([])"), True)
