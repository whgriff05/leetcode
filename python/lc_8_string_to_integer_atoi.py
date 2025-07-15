def myAtoi(s):
    current_number = 0
    is_negative = False
    is_positive = False
    first_number_read = False

    for char in s:
        if char == " ":
            if first_number_read or is_positive or is_negative:
                break
            continue
        elif char == "-" and not first_number_read and not is_positive and not is_negative:
            is_negative = True
        elif char == "-" and first_number_read:
            break
        elif char == "+" and not first_number_read and not is_negative and not is_positive:
            is_positive = True
            is_negative = False
        elif char == "+" and first_number_read:
            break
        elif char not in "0123456789":
            break
        if char in "0123456789":
            first_number_read = True
            current_number *= 10
            current_number += int(char)
            

    if is_negative:
        current_number *= -1

    if current_number > (2**31 - 1):
        current_number = 2**31 - 1
    elif current_number < (-2**31):
        current_number = -2**31

    print(current_number)
    return current_number


# Tests
from testsuite import lc_test
lc_test(1, myAtoi("42"), 42)
lc_test(2, myAtoi(" -042"), -42)
lc_test(3, myAtoi("1337c0d3"), 1337)
lc_test(4, myAtoi("0-1"), 0)
lc_test(5, myAtoi("words and 987"), 0)
lc_test(6, myAtoi("+-12"), 0)
lc_test(7, myAtoi("-+12"), 0)
