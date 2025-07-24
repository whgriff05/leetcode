from testsuite import ListNode
def deleteNode(node):
    node.val = node.nxt.val
    node.nxt = node.nxt.nxt


# Tests
from testsuite import lc_test, list_to_linked_list
head = list_to_linked_list([4, 5, 1, 9])
node = head.nxt
deleteNode(node)
lc_test(1, head, list_to_linked_list([4, 1, 9]))

head2 = list_to_linked_list([4, 5, 1, 9])
node2 = head2.nxt.nxt
deleteNode(node2)
lc_test(2, head2, list_to_linked_list([4, 5, 9]))
