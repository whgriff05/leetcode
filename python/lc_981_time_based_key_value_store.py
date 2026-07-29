class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value , timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dic.get(key , [])
        l , r = 0 , len(values) - 1
        while l <= r :
            mid = (l + r) >> 1
            if values[mid][1] <= timestamp:
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1
        return res

# Tests
from testsuite import lc_test

tm = TimeMap()
tm.set("foo", "bar", 1)
lc_test(1, tm.get("foo", 1), "bar")
lc_test(2, tm.get("foo", 3), "bar")
tm.set("foo", "bar2", 4)
lc_test(3, tm.get("foo", 4), "bar2")
lc_test(3, tm.get("foo", 5), "bar2")

