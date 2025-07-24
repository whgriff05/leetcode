def merge(intervals):
    intervals.sort()
    output = []
    for interval in intervals:
        if len(output) == 0:
            output.append(interval)
            continue

        if interval[0] < output[-1][1] and interval[1] <= output[-1][1]:
            continue
        elif interval[0] <= output[-1][1] and interval[1] > output[-1][1]:
            output[-1] = [output[-1][0], interval[1]]

        elif interval[0] > output[-1][1]:
            output.append(interval)

    print(output)
    return output


# Tests
from testsuite import lc_test
lc_test(1, merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
lc_test(2, merge([[1, 4], [4, 5]]), [[1, 5]])
lc_test(3, merge([[1, 4], [0, 4]]), [[0, 4]])
lc_test(4, merge([[1, 4], [0, 5]]), [[0, 5]])
lc_test(5, merge([[1, 4], [0, 0]]), [[0, 0], [1, 4]])
