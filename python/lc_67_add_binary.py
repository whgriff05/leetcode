def addBinary(a, b):
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    output = ""
    while i >= 0 or j >= 0 or carry > 0:
        ca = int(a[i]) if i >= 0 else 0
        cb = int(b[j]) if j >= 0 else 0

        sum = ca + cb + carry
        output = f"{sum % 2}{output}"
        carry = sum // 2

        i -= 1
        j -= 1

    return output


# Tests
from testsuite import lc_test
lc_test(1, addBinary("11", "1"), "100")
lc_test(2, addBinary("1010", "1011"), "10101")
