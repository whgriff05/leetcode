class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        x = self.q1.pop(0)

        while len(self.q2) > 0:
            self.q1.append(self.q2.pop(0))

        return x

    def top(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        x = self.q1.pop(0)
        self.q2.append(x)

        while len(self.q2) > 0:
            self.q1.append(self.q2.pop(0))

        return x

    def empty(self):
        return len(self.q1) == 0


# Tests
from testsuite import lc_test

ms = MyStack()
ms.push(1)
ms.push(2)

lc_test(1, ms.top(), 2)
lc_test(2, ms.pop(), 2)
lc_test(3, ms.empty(), False)

