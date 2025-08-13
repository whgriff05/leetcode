from testsuite import TreeNode

def isBalanced(root):
    if root is None:
        return True

    def get_height(root):
        if root is None:
            return 0

        left = get_height(root.left)
        right = get_height(root.right)

        return 1 + max(left, right)

    if isBalanced(root.left) and isBalanced(root.right) and abs(get_height(root.left) - get_height(root.right)) <= 1:
        return True
    return False

# Tests
from testsuite import lc_test
t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
lc_test(1, isBalanced(t1), True)

t2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
lc_test(2, isBalanced(t2), False)

t3 = None
lc_test(3, isBalanced(t3), True)

t4 = TreeNode(1)
lc_test(4, isBalanced(t4), True)
