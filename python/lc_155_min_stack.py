class MinStack:
    
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val):
        if len(self.stack) == 0:
            self.mins.append(val)
        else:
            if val < self.mins[-1]:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[-1])
                
        self.stack.append(val)

    def pop(self):
        self.mins.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mins[-1]


# Tests
from testsuite import lc_test

ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)

lc_test(1, ms.getMin(), -3)

ms.pop()
lc_test(2, ms.top(), 0)
lc_test(3, ms.getMin(), -2)



ms2 = MinStack()
ms2.push(2)
ms2.push(0)
ms2.push(2)
ms2.push(3)

lc_test(4, ms2.getMin(), 0)

ms2.pop()
lc_test(5, ms2.getMin(), 0)

ms2.pop()
lc_test(6, ms2.getMin(), 0)

ms2.pop()
lc_test(7, ms2.getMin(), 2)
