def reverseStr(s, k):
    ls = list(s)

    for i in range(0, len(ls), 2*k):
        ls[i:i+k] = reversed(ls[i:i+k])

    return "".join(ls)
    
            
    
    


# Tests
from testsuite import lc_test
lc_test(1, reverseStr("abcdefg", 2), "bacdfeg")
lc_test(2, reverseStr("abcd", 2), "bacd")
