def plusOne(digits):
    n = 0
    for d in digits:
        n *= 10
        n += d

    n += 1

    output = []
    while n > 0:
        output.insert(0, n % 10)
        n //= 10

    return output


# Tests
from testsuite import lc_test

lc_test(1, plusOne([1, 2, 3]), [1, 2, 4])
lc_test(2, plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
lc_test(3, plusOne([9]), [1, 0])
