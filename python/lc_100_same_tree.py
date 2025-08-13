from testsuite import TreeNode

def isSameTree(p, q):
    if ((not p) and q) or (p and (not q)):
        return False

    if (not p) and (not q):
        return True

    left = isSameTree(p.left, q.left)
    right = isSameTree(p.right, q.right)

    return left and right and p.val == q.val


# Tests
from testsuite import lc_test
t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(2), TreeNode(3))
lc_test(1, isSameTree(t1, t2), True)

t1 = TreeNode(1, TreeNode(2))
t2 = TreeNode(1, None, TreeNode(2))
lc_test(2, isSameTree(t1, t2), False)

t1 = TreeNode(1, TreeNode(2), TreeNode(1))
t2 = TreeNode(1, TreeNode(1), TreeNode(2))
lc_test(3, isSameTree(t1, t2), False)

t1 = None
t2 = None
lc_test(4, isSameTree(t1, t2), True)

