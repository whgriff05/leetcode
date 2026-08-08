def findDiagonalOrder(mat):
    if not mat: return []
    if not mat[0]: return []
    output = []

    rows, cols = len(mat), len(mat[0])
    x, y = 0, 0
    up = True

    for _ in range(rows * cols):
        output.append(mat[y][x])

        if up:
            if x == cols - 1: # Right side
                y += 1
                up = False

            elif y == 0: # Top edge
                x += 1
                up = False

            else:
                x += 1
                y -= 1

        else:
            if y == rows - 1: # Bottom edge
                x += 1
                up = True

            elif x == 0: # Left side
                y += 1
                up = True

            else:
                x -= 1
                y += 1

    return output

# Tests
from testsuite import lc_test

lc_test(1, findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 4, 7, 5, 3, 6, 8, 9], sort_lists=False)

lc_test(2, findDiagonalOrder([[1, 2], [3, 4]]), [1, 2, 3, 4], sort_lists=False)
