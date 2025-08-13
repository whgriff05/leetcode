from testsuite import TreeNode

def diameterOfBinaryTree(root):
    result = [0]

    def dfs(root):
        if root == None:
            return -1

        left = dfs(root.left)
        right = dfs(root.right)

        result[0] = max(result[0], 2 + left + right)

        return 1 + max(left, right)

    dfs(root)
    return result[0]
        
    


# Tests
from testsuite import lc_test
t1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
lc_test(1, diameterOfBinaryTree(t1), 3)

t2 = TreeNode(1, TreeNode(2))
lc_test(2, diameterOfBinaryTree(t2), 1)
