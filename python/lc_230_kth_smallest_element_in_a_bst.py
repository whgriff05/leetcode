from testsuite import TreeNode

def kthSmallest(root, k):
    stack = []

    while root:
        stack.append(root)
        root = root.left

    for i in range(k-1):
        root = stack.pop()
        root = root.right
        while root:
            stack.append(root)
            root = root.left

    return stack[-1].val
        


# Tests
from testsuite import lc_test

t1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
lc_test(1, kthSmallest(t1, 1), 1)

t2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
lc_test(2, kthSmallest(t2, 3), 3)
