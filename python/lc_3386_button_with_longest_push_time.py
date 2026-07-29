def buttonWithLongestTime(events):
    # Faster solution
    cmb = events[0][0]
    cmt = events[0][1]

    for i in range(len(events)):
        if events[i][1] - events[i-1][1] > cmt:
            cmt = events[i][1] - events[i-1][1] 
            cmb = events[i][0]
        elif events[i][1] - events[i-1][1] == cmt:
            cmb = min(cmb, events[i][0])

    return cmb


def OLDbuttonWithLongestTime(events):
    # Slower original solution
    current_max_button = events[0][0]
    current_max_time = events[0][1]

    for i, pair in enumerate(events[1:], 1):
        if pair[1] - events[i-1][1] > current_max_time:
            current_max_time = pair[1] - events[i-1][1]
            current_max_button = pair[0]
        elif pair[1] - events[i-1][1] == current_max_time:
            current_max_button = min(pair[0], current_max_button)
    
    return current_max_button


# Tests
from testsuite import lc_test

lc_test(1, buttonWithLongestTime([[1, 2], [2, 5], [3, 9], [1, 15]]), 1)

lc_test(2, buttonWithLongestTime([[10, 5], [1, 7]]), 10)
