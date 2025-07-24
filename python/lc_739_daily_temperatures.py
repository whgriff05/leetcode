def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
        
    return result
        
        
    


# Tests
from testsuite import lc_test
lc_test(1, dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
lc_test(2, dailyTemperatures([30,40,50,60]), [1,1,1,0])
lc_test(3, dailyTemperatures([30,60,90]), [1,1,0])
