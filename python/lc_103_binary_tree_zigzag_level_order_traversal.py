from testsuite import TreeNode

def zigzagLevelOrder(root):
    output = []
    if not root:
        return output

    queue = {root: 0}
    
    while queue:
        qkeys = list(queue.keys())
        if qkeys[0].left:
            queue[qkeys[0].left] = queue[qkeys[0]] + 1

        if qkeys[0].right:
            queue[qkeys[0].right] = queue[qkeys[0]] + 1

        value = qkeys[0].val
        level = queue[qkeys[0]]
        del queue[qkeys[0]]

        if len(output) == level:
            output.append([])

        if level % 2 == 0:
            output[level].append(value)
        else:
            output[level].insert(0, value)
        
    return output
    


# Tests
from testsuite import lc_test

t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
lc_test(1, zigzagLevelOrder(t1), [[3], [20, 9], [15, 7]])

t2 = TreeNode(1)
lc_test(2, zigzagLevelOrder(t2), [[1]])

t3 = None
lc_test(3, zigzagLevelOrder(t3), [])
