from testsuite import TreeNode

def postorderTraversal(root):
    output = []
    if not root:
        return output

    output = output + postorderTraversal(root.left)
    output = output + postorderTraversal(root.right)
    output = output + [root.val]


    return output



# Tests
from testsuite import lc_test

t1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
lc_test(1, postorderTraversal(t1), [3, 2, 1])

t2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, None, TreeNode(8, TreeNode(9))))
lc_test(2, postorderTraversal(t2), [4, 6, 7, 5, 2, 9, 8, 3, 1])

t3 = None
lc_test(3, postorderTraversal(t3), [])

t4 = TreeNode(1)
lc_test(4, postorderTraversal(t4), [1])

