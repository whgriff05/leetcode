def generateMatrix(n):
    if n == 0: return []
    matrix = [[0] * n for _ in range(n)]

    count = 1

    min_i, max_i = 0, len(matrix[0]) - 1
    min_j, max_j = 0, len(matrix) - 1

    while min_i <= max_i and min_j <= max_j:
        # Top row, move down:
        for i in range(min_i, max_i+1):
            matrix[min_j][i] = count
            count += 1
        min_j += 1

        # Right col, move left
        for j in range(min_j, max_j+1):
            matrix[j][max_i] = count
            count += 1
        max_i -= 1

        # Bottom row, move up
        for i in range(max_i, min_i-1, -1):
            matrix[max_j][i] = count
            count += 1
        max_j -= 1

        # Left col, move right
        for j in range(max_j, min_j-1, -1):
            matrix[j][min_i] = count
            count += 1
        min_i += 1

    return matrix


# Tests
from testsuite import lc_test

lc_test(1, generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]], sort_lists=False)

lc_test(2, generateMatrix(1), [[1]], sort_lists=False)
