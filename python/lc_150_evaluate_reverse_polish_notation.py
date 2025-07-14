def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            val1 = stack.pop()
            val2 = stack.pop()
            match token:
                case "+":
                    stack.append(val2 + val1)
                case "-":
                    stack.append(val2 - val1)
                case "*":
                    stack.append(val2 * val1)
                case "/":
                    stack.append(int(val2 / val1))
        else:
            stack.append(int(token))

    return stack[0]


# Tests
from testsuite import lc_test

lc_test(1, evalRPN(["2", "1", "+", "3", "*"]), 9)
lc_test(2, evalRPN(["4", "13", "5", "/", "+"]), 6)
lc_test(3, evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
