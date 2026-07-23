def divide(dividend, divisor):
    if divisor == 1:
        return dividend

    if dividend == -(2**31) and divisor == -1:
        return 2**31 - 1

    sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

    dividend = -dividend if dividend > 0 else dividend
    divisor = -divisor if divisor > 0 else divisor

    result = 0
    while dividend <= divisor:
        x = divisor
        count = 1
        while x >= (-(2**30)) and dividend <= (x << 1):
            x <<= 1
            count <<= 1

        dividend -= x
        result += count


    return result if sign else -result


# Tests
from testsuite import lc_test
lc_test(1, divide(10, 3), 3)
lc_test(2, divide(7, -3), -2)

