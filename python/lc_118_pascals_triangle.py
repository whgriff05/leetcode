def generate(numRows):
    output = [[1]]
    if numRows == 1:
        return output
    elif numRows == 2:
        output.append([1, 1])
        return output

    output.append([1, 1])
    for i in range(numRows-2):
        prev_row = i + 1
        curr_row = [1]
        for i in range(1, i+2):
            curr_row.append(output[prev_row][i-1] + output[prev_row][i])
        curr_row.append(1)
        output.append(curr_row)

    return output


# Tests
from testsuite import lc_test
lc_test(1, generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
lc_test(2, generate(1), [[1]])
