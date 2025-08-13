from testsuite import TreeNode

def maxDepth(root):
    if root == None:
        return 0

    depth_left = maxDepth(root.left) + 1
    depth_right = maxDepth(root.right) + 1
    return max(depth_left, depth_right)
    


# Tests
from testsuite import lc_test
t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
lc_test(1, maxDepth(t1), 3)

t2 = TreeNode(1, None, TreeNode(2))
lc_test(2, maxDepth(t2), 2)
