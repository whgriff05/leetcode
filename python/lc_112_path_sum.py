from testsuite import TreeNode

def hasPathSum(root, targetSum):
    if root is None:
        return False

    def dfs(root, target):
        # Base case: leaf node
        if root.left == None and root.right == None:
            return target == root.val

        # Recursive case 1: only left node
        if not root.right:
            return dfs(root.left, target - root.val)

        # Recursive case 2: only right node
        if not root.left:
            return dfs(root.right, target - root.val)

        # Recursive case 3: both child nodes
        return dfs(root.left, target-root.val) or dfs(root.right, target-root.val)

    return dfs(root, targetSum)








# Tests

from testsuite import lc_test

t1 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
lc_test(1, hasPathSum(t1, 22), True)

t2 = TreeNode(1, TreeNode(2), TreeNode(3))
lc_test(2, hasPathSum(t2, 5), False)

t3 = None
lc_test(3, hasPathSum(t3, 0), False)

t4 = TreeNode(1, TreeNode(2))
lc_test(4, hasPathSum(t4, 1), False)
