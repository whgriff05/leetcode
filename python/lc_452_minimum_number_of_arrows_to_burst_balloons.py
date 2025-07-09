def findMinArrowShots(points):
    arrows = 0
    points.sort()
    while points:
        if len(points) == 1 or points[0][1] < points[1][0]:
            arrows += 1
            del points[0]
        else:
            overlap_point = [points[1][0], min(points[0][1], points[1][1])]
            points[0] = overlap_point
            del points[1]
    return arrows
        
def neetcode(points):
    points.sort()

    res = len(points)
    prev = points[0]
    for i in range(1, len(points)):
        curr = points[i]

        if curr[0] <= prev[1]:
            res -= 1
            prev = [curr[0], min(curr[1], prev[1])]
        else:
            prev = curr

    return res

# Tests
from testsuite import lc_test
lc_test(1, findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]), 2)
lc_test(2, findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]), 4)
lc_test(3, findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]), 2)
