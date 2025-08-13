def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]

    prev = getRow(rowIndex - 1)
    new = []
    new.append(1)
    for i in range(rowIndex - 1):
        new.append(prev[i] + prev[i+1])
    new.append(1)

    return new


# Tests
from testsuite import lc_test
lc_test(1, getRow(3), [1, 3, 3, 1])
lc_test(2, getRow(0), [1])
lc_test(3, getRow(1), [1, 1])
