from testsuite import Node

def postorder(root):
    output = []
    if not root:
        return output

    if root.children:
        for i in range(len(root.children)):
            output = output + postorder(root.children[i])
    output = output + [root.val]

    return output



# Tests
from testsuite import lc_test

n1 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
lc_test(1, postorder(n1), [5, 6, 3, 2, 4, 1])

n2 = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
lc_test(2, postorder(n2), [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1])


