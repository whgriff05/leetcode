def flipAndInvertImage(image):
    new = []

    for row in image:
        r = [1 if v == 0 else 0 for v in row]
        r = r[::-1]
        new.append(r)

    return new

    


# Tests
from testsuite import lc_test
lc_test(1, flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]), [[1, 0, 0], [0, 1, 0], [1, 1, 1]])
lc_test(2, flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]), [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]])
