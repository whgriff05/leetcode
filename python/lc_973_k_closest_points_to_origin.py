import heapq
import math

def kClosest(points, k):
    heap = []
    for i, point in enumerate(points):
        dist = math.sqrt(point[0]**2 + point[1]**2)

        heapq.heappush(heap, (dist, i))

    output = []
    for i in range(k):
        d, idx = heapq.heappop(heap)
        output.append(points[idx])

    return output


# Tests
from testsuite import lc_test

lc_test(1, kClosest([[1,3], [-2,2]], 1), [[-2,2]])
lc_test(2, kClosest([[3,3], [5,-1], [-2,4]], 2), [[3,3], [-2,4]])
