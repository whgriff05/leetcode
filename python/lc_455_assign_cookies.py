def findContentChildren(g, s):
    output = 0
    g.sort()
    g.reverse()
    s.sort()
    s.reverse()
    g_counter = 0
    s_counter = 0

    while g_counter < len(g) and s_counter < len(s):
        if g[g_counter] <= s[s_counter]:
            output += 1
            g_counter += 1
            s_counter += 1
        else:
            g_counter += 1

    return output


# Tests
from testsuite import lc_test
lc_test(1, findContentChildren([1, 2, 3], [1, 1]), 1)
lc_test(2, findContentChildren([1, 2], [1, 2, 3]), 2)
