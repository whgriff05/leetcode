def rotate(matrix):
    if len(matrix) == 1: return

    # Transpose matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            holder = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = holder

    # Reverse rows
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]


# Tests
from testsuite import lc_test

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(x)
lc_test(1, x, [[7, 4, 1], [8, 5, 2], [9, 6, 3]], sort_lists=False)

y = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(y)
lc_test(2, y, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], sort_lists=False)
