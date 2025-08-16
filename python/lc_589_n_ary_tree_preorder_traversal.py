from testsuite import Node

def preorder(root):
    output = []
    if not root:
        return output

    output = output + [root.val]
    if root.children:
        for i in range(len(root.children)):
            output = output + preorder(root.children[i])

    return output



# Tests
from testsuite import lc_test

n1 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
lc_test(1, preorder(n1), [1, 3, 5, 6, 2, 4])

n2 = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
lc_test(2, preorder(n2), [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10])


