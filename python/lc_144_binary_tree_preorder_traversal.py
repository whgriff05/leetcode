from testsuite import TreeNode

def preorderTraversal(root):
    output = []
    if not root:
        return output

    output = output + [root.val]
    output = output + preorderTraversal(root.left)
    output = output + preorderTraversal(root.right)

    return output



# Tests
from testsuite import lc_test

t1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
lc_test(1, preorderTraversal(t1), [1, 2, 3])

t2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, None, TreeNode(8, TreeNode(9))))
lc_test(2, preorderTraversal(t2), [1, 2, 4, 5, 6, 7, 3, 8, 9])

t3 = None
lc_test(3, preorderTraversal(t3), [])

t4 = TreeNode(1)
lc_test(4, preorderTraversal(t4), [1])

