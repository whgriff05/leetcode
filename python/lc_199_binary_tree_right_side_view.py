from testsuite import TreeNode

def rightSideView(root):
    if not root:
        return []

    output = []
    queue = {root: 0}

    while queue:
        qkeys = list(queue.keys())
        if qkeys[0].left:
            queue[qkeys[0].left] = queue[qkeys[0]] + 1

        if qkeys[0].right:
            queue[qkeys[0].right] = queue[qkeys[0]] + 1

        tv = qkeys[0].val
        tlevel = queue[qkeys[0]]
        del queue[qkeys[0]]

        if len(output) == tlevel:
            output.append([])

        output[tlevel].append(tv)

    res = []
    for a in output:
        res.append(a[-1])

    return res

    


# Tests
from testsuite import lc_test

t1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
lc_test(1, rightSideView(t1), [1, 3, 4])

t2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
lc_test(2, rightSideView(t2), [1, 3, 4, 5])

t3 = TreeNode(1, None, TreeNode(3))
lc_test(3, rightSideView(t3), [1, 3])

t4 = None
lc_test(4, rightSideView(t4), [])
