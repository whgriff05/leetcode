def carPooling(trips, capacity):
    itinerary = {}
    # stop: [pick up, drop off]

    for trip in trips:
        # pick ups
        if trip[1] not in itinerary:
            itinerary[trip[1]] = [trip[0], 0]
        else:
            itinerary[trip[1]][0] += trip[0]

        # drop offs
        if trip[2] not in itinerary:
            itinerary[trip[2]] = [0, trip[0]]
        else:
            itinerary[trip[2]][1] += trip[0]

    itinerary = dict(sorted(itinerary.items()))

    current = 0
    for stop in itinerary:
        current += itinerary[stop][0]
        current -= itinerary[stop][1]
        if current > capacity:
            return False
    return True
        



# Tests
from testsuite import lc_test
lc_test(1, carPooling([[2, 1, 5], [3, 3, 7]], 4), False)
lc_test(2, carPooling([[2, 1, 5], [3, 3, 7]], 5), True)
