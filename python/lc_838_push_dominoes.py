import math
from collections import deque


def pushDominoes(dominoes):
    dom = list(dominoes)
    q = deque()

    for i, d in enumerate(dom):
        if d != ".":
            q.append((i, d))

    while q:
        i, d = q.popleft()
        if d == "L":
            if i > 0 and dom[i-1] == ".":
                q.append((i-1, "L"))
                dom[i-1] = "L"
        else:
            if i + 1 < len(dom) and dom[i+1] == ".":
                if i + 2 < len(dom) and dom[i+2] == "L":
                    q.popleft()
                else:
                    q.append((i+1, "R"))
                    dom[i+1] = "R"

    return "".join(dom)
                                

def NAIVEpushDominoes(dominoes):
    output = ""
    for i in range(len(dominoes)):
        if dominoes[i] == "R" or dominoes[i] == "L":
            output += dominoes[i]
            continue

        lean_right = i
        lean_left = i

        while lean_right >= 0:
            if dominoes[lean_right] == "R":
                lean_right = abs(lean_right - i)
                break
            elif dominoes[lean_right] == "L":
                lean_right = math.inf
                break
            lean_right -= 1
        if lean_right < 0:
            lean_right = math.inf

        while lean_left < len(dominoes):
            if dominoes[lean_left] == "L":
                lean_left = abs(lean_left - i)
                break
            if dominoes[lean_left] == "R":
                lean_left = math.inf
                break
            lean_left += 1
        if lean_left >= len(dominoes):
            lean_left = math.inf

        if lean_right > lean_left:
            output += "L"
        elif lean_right < lean_left:
            output += "R"
        else:
            output += "."
        

    return output

# Tests
from testsuite import lc_test
lc_test(1, pushDominoes("RR.L"), "RR.L")
lc_test(2, pushDominoes(".L.R...LR..L.."), "LL.RR.LLRRLL..")
