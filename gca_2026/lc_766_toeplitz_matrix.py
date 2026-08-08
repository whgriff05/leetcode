def isToeplitzMatrix(matrix):
    cx = 0
    cy = len(matrix) - 1
    up = True
    rows = len(matrix)
    cols = len(matrix[0])
    current = matrix[cy][cx]

    for _ in range(rows * cols):
        if matrix[cy][cx] != current:
            return False

        if up:
            if cy == 0: # Top Edge
                up = False
                cx += 1
                cx = min(cx, cols - 1)
                current = matrix[cy][cx]
            elif cx == 0:
                up = False
                cy -= 1
                cy = max(cy, 0)
                current = matrix[cy][cx]
            else:
                cx -= 1
                cy -= 1
        else:
            if cx == cols - 1:
                up = True
                cy -= 1
                cy = max(cy, 0)
                current = matrix[cy][cx]
            elif cy == rows - 1:
                up = True
                cx += 1
                cx = min(cx, cols - 1)
                current = matrix[cy][cx]
            else:
                cx += 1
                cy += 1

    return True


# Tests
from testsuite import lc_test


lc_test(1, isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]), True)

lc_test(2, isToeplitzMatrix([[1, 2], [2, 2]]), False)

lc_test(3, isToeplitzMatrix([[84]]), True)
