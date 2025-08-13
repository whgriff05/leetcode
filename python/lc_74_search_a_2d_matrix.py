def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
        return False

    search_row = 0

    left_rows = 0
    right_rows = len(matrix) - 1
    while left_rows <= right_rows:
        mid_rows = (left_rows + right_rows) // 2
        if matrix[mid_rows][-1] >= target and matrix[mid_rows - 1][-1] < target:
            search_row = mid_rows

        if matrix[mid_rows][-1] < target:
            left_rows = mid_rows + 1
        else:
            right_rows = mid_rows - 1


    left_cols = 0
    right_cols = len(matrix[0]) - 1
    while left_cols <= right_cols:
        mid_cols = (left_cols + right_cols) // 2
        if matrix[search_row][mid_cols] == target:
            return True

        if matrix[search_row][mid_cols] < target:
            left_cols = mid_cols + 1
        else:
            right_cols = mid_cols - 1

    return False



# Tests
from testsuite import lc_test
lc_test(1, searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True)
lc_test(2, searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False)
