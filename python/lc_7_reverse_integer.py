def reverse(x):
    is_negative = x < 0
    if is_negative:
        x = x * -1

    tx = list(map(int, str(x)))
    tx.reverse()
    out = 0
    while tx:
        out *= 10
        out += tx[0]
        del tx[0]

    if is_negative:
        out *= -1

    if out > (2**31 -1) or out < -1 * (2**31):
        return 0
    
    return out
    

# Tests
from testsuite import lc_test
lc_test(1, reverse(123), 321)
lc_test(2, reverse(-123), -321)
lc_test(3, reverse(120), 21)
