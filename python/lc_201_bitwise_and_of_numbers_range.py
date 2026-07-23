def rangeBitwiseAnd(left, right):
    left_s = f"{left:032b}"
    right_s = f"{right:032b}"

    prev_change = False
    output = ""

    for i in range(32):
        lc = left_s[i]
        rc = right_s[i]
        
        if lc != rc:
            prev_change = True
            output = f"{output}0"
        else:
            if prev_change:
                output = f"{output}0"
            else:
                if lc == "1":
                    output = f"{output}1"
                else:
                    output = f"{output}0"
                

    return int(output, 2)



# Tests
from testsuite import lc_test
lc_test(1, rangeBitwiseAnd(5, 7), 4)
"""
5| 101
6| 110
7| 111
-|----
   100

"""


lc_test(1, rangeBitwiseAnd(0, 0), 0)
lc_test(1, rangeBitwiseAnd(1, 2147483647), 0)
