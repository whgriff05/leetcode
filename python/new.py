#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3

import sys

with open(f"{sys.argv[1]}.py", "w") as f:
    f.write(f"def {sys.argv[2]}():\n")
    f.write("    pass\n")
    f.write("\n")
    f.write("# Tests\n")
    f.write("from testsuite import lc_test\n")
    for i in range(int(sys.argv[3])):
        f.write(f"lc_test({i+1}, {sys.argv[2]}(), )\n")
        
