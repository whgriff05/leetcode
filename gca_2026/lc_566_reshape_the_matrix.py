def matrixReshape(mat, r, c):
    if r * c != len(mat) * len(mat[0]):
        return mat

    if r == len(mat) and c == len(mat[0]):
        return mat

    new = [[0] * c for _ in range(r)]
    cx, cy = 0, 0

    for row in mat:
        for item in row:
            new[cy][cx] = item

            if cx == len(new[0])-1:
                cy += 1
                cx = 0
            else:
                cx += 1

    return new



# Tests
from testsuite import lc_test

lc_test(1, matrixReshape([[1, 2], [3, 4]], 1, 4), [[1, 2, 3, 4]])
lc_test(2, matrixReshape([[1, 2], [3, 4]], 2, 2), [[1, 2], [3, 4]])
lc_test(3, matrixReshape([[1, 2], [3, 4]], 4, 1), [[1], [2], [3], [4]])

