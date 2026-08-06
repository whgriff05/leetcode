import collections

def numPairsDivisibleBy60(time):
    total = 0
    c = collections.Counter()

    for t in time:
        other = (60 - t) % 60

        total += c[other]
        c[t % 60] += 1
    return total






# Tests
from testsuite import lc_test

lc_test(1, numPairsDivisibleBy60([30, 20, 150, 100, 40]), 3)
lc_test(2, numPairsDivisibleBy60([60, 60, 60]), 3)
