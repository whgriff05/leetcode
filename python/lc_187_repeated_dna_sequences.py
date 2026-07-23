def findRepeatedDnaSequences(s):
    if len(s) <= 10:
        return []

    ht = {}

    i = 0
    j = 10

    while j <= len(s):
        section = s[i:j]
        ht[section] = ht.get(section, 0) + 1
        i += 1
        j += 1

    return [section for section, count in ht.items() if count > 1]

# Tests
from testsuite import lc_test
lc_test(1, findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC", "CCCCCAAAAA"])

lc_test(2, findRepeatedDnaSequences("AAAAAAAAAAAAA"), ["AAAAAAAAAA"])
