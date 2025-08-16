from testsuite import TreeNode

def isSymmetric(root):
    left = []
    right = []
    lqueue = []
    rqueue = []

    if root.left:
        lqueue = [root.left]

    while lqueue:
        current_node = lqueue.pop(0)
        if current_node:
            lqueue.append(current_node.left)
            lqueue.append(current_node.right)
            
        if current_node:
            left.append(current_node.val)
        else:
            left.append(None)
        
        
    if root.right:
        rqueue = [root.right]

    while rqueue:
        current_node = rqueue.pop(0)
        if current_node:
            rqueue.append(current_node.right)
            rqueue.append(current_node.left)

        if current_node:
            right.append(current_node.val)
        else:
            right.append(None)

    return left == right       


# Tests
from testsuite import lc_test

t1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
lc_test(1, isSymmetric(t1), True)

t2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
lc_test(2, isSymmetric(t2), False)
