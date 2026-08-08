def canFormArray(arr, pieces):
    head = 0 
    t = []
    while pieces:
        # find piece that has next number of head
        # check contents
        # add piece
        for i, p in enumerate(pieces):
            if p[0] == arr[head]:
                break
        piece = pieces.pop(i)
        if arr[head:head+len(piece)] == piece:
            t += piece
        else:
            return False

        head += len(piece)

    return True


# Tests

from testsuite import lc_test

lc_test(1, canFormArray([15, 88], [[88], [15]]), True)

lc_test(2, canFormArray([49, 18, 16], [[16, 18, 49]]), False)

lc_test(3, canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]), True)
