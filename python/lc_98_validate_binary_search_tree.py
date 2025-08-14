from testsuite import TreeNode

def isValidBST(root):
    def valid(node, left, right):
        if not node:
            return True

        if not (node.val < right and node.val > left):
            return False

        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    return valid(root, float("-inf"), float("inf "))

# Tests
from testsuite import lc_test

t1 = TreeNode(2, TreeNode(1), TreeNode(3))
lc_test(1, isValidBST(t1), True)

t2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
lc_test(2, isValidBST(t2), False)

t3 = TreeNode(1, TreeNode(1))
lc_test(3, isValidBST(t3), False)

t4 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
lc_test(4, isValidBST(t4), False)
