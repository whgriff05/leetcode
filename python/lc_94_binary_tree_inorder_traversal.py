from testsuite import TreeNode

def inorderTraversal(root):
    output = []
    if not root:
        return output

    if root.left:
        output = inorderTraversal(root.left) + output

    output = output + [root.val]

    if root.right:
        output = output + inorderTraversal(root.right)

    return output

    

# Tests
from testsuite import lc_test

t1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
lc_test(1, inorderTraversal(t1), [1, 3, 2])

t2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, None, TreeNode(8, TreeNode(9))))
lc_test(2, inorderTraversal(t2), [4, 2, 6, 5, 7, 1, 3, 9, 8])

t3 = None
lc_test(3, inorderTraversal(t3), [])

t4 = TreeNode(1)
lc_test(4, inorderTraversal(t4), [1])
