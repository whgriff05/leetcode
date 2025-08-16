from testsuite import Node

def levelOrder(root):
    output = []
    if not root:
        return output

    queue = {root: 0}

    while queue:
        qkeys = list(queue.keys())
        current = qkeys[0]

        if current.children:
            for i in range(len(current.children)):
                queue[current.children[i]] = queue[current] + 1

        value = current.val
        level = queue[current]
        del queue[current]

        if len(output) == level:
            output.append([])

        output[level].append(value)

    return output

    


# Tests
from testsuite import lc_test

n1 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
lc_test(1, levelOrder(n1), [[1], [3, 2, 4], [5, 6]])


n2 = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
lc_test(2, levelOrder(n2), [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]])
