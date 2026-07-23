def grayCode(n):
    output = []

    for i in range((1 << n)):
        output.append(i ^ (i >> 1))

    return output


# Tests
from testsuite import lc_test, int_to_binary_str
lc_test(1, grayCode(2), [0, 1, 3, 2])
lc_test(2, grayCode(1), [0, 1])
lc_test(3, grayCode(3), [0, 1, 3, 7, 5, 4, 6, 2])

print([int_to_binary_str(g, 4) for g in grayCode(4)])

# n = 3 | 000, 100, 101, 111, 110, 010, 011, 001
# OR
# n = 3 | 000, 001, 011, 010, 110, 111, 101, 100
# n = 3 | 000, 001, 011, 111, 101, 100, 110, 010

# n = 2 | 10 XOR 01 = 0
