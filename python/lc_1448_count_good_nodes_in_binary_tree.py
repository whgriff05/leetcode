from testsuite import TreeNode

def goodNodes(root):
    good = 0

    def dfs(node, max_val):
        if not node:
            return 0

        res = 1 if node.val >= max_val else 0
        max_val = max(node.val, max_val)

        res += dfs(node.left, max_val)
        res += dfs(node.right, max_val)

        return res
        


    good = dfs(root, root.val)
    return good

    


# Tests
from testsuite import lc_test
t1 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
lc_test(1, goodNodes(t1), 4)

t2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
lc_test(2, goodNodes(t2), 3)

t3 = TreeNode(1)
lc_test(3, goodNodes(t3), 1)

t4 = None
lc_test(4, goodNodes(t4), 0)
