def spiralOrder(matrix):
    if not matrix: return []
    output = []
    min_i, max_i = 0, len(matrix[0]) - 1
    min_j, max_j = 0, len(matrix) - 1

    while min_i <= max_i and min_j <= max_j:
        # Add top row and move down
        for i in range(min_i, max_i+1):
            output.append(matrix[min_j][i])
        min_j += 1
        print(min_j, max_j, output)

        # Add right side and move left
        for j in range(min_j, max_j+1):
            output.append(matrix[j][max_i])
        max_i -= 1
        print(min_i, max_i, output)

        # Add bottom row and move up
        if min_j <= max_j:
            for i in range(max_i, min_i-1, -1):
                output.append(matrix[max_j][i])
            max_j -= 1
            print(min_j, max_j, output)

        # Add left side and move right
        if min_i <= max_i:
            for j in range(max_j, min_j-1, -1):
                output.append(matrix[j][min_i])
            min_i += 1
            print(min_i, max_i, output)

    return output


# Tests
from testsuite import lc_test

lc_test(1, spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5], sort_lists=False)

lc_test(2, spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], sort_lists=False)

lc_test(3, spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]), [1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10], sort_lists=False)
