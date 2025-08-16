from testsuite import TreeNode

def flipMatchVoyage(root, voyage):
    i = 0
    output = []
    stack = [root]

    while stack:
        curr = stack.pop()

        if curr.val != voyage[i]:
            return [-1]

        i += 1
        if curr.left and curr.left.val != voyage[i]:
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

            output.append(curr.val)
        else:
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)



    return output
                
                

# Tests
from testsuite import lc_test

t1 = TreeNode(1, TreeNode(2))
lc_test(1, flipMatchVoyage(t1, [2, 1]), [-1])

t2 = TreeNode(1, TreeNode(2), TreeNode(3))
lc_test(2, flipMatchVoyage(t2, [1, 3, 2]), [1])

t3 = TreeNode(1, TreeNode(2), TreeNode(3))
lc_test(3, flipMatchVoyage(t3, [1, 2, 3]), [])

t4 = TreeNode(1, TreeNode(2, TreeNode(3)))
lc_test(4, flipMatchVoyage(t4, [1, 3, 2]), [-1])
