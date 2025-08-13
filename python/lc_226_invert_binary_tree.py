from testsuite import TreeNode

def invertTree(root):
    if root == None:
        return None

    temp = invertTree(root.left)
    root.left = invertTree(root.right)
    root.right = temp

    return root



# Tests
from testsuite import lc_test
t1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
t1_invert = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
lc_test(1, invertTree(t1), t1_invert)

t2 = TreeNode(2, TreeNode(1), TreeNode(3))
t2_invert = TreeNode(2, TreeNode(3), TreeNode(1))
lc_test(2, invertTree(t2), t2_invert)

t3 = TreeNode(None)
t3_invert = TreeNode(None)
lc_test(3, invertTree(t3), t3_invert)
