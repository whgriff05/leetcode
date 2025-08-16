from testsuite import TreeNode

def levelOrderBottom(root):
    if root is None:
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

    output = output[::-1]

    return output


# Tests
from testsuite import lc_test

t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
lc_test(1, levelOrderBottom(t1), [[15, 7], [9, 20], [3]])

t2 = TreeNode(1)
lc_test(2, levelOrderBottom(t2), [[1]])

t3 = None
lc_test(3, levelOrderBottom(t3), [])
