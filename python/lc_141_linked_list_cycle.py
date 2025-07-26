from testsuite import ListNode

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.nxt:
        fast = fast.nxt.nxt
        slow = slow.nxt

        if slow == fast:
            return True

    return False
        



# Tests
from testsuite import lc_test, list_to_linked_list
l1 = ListNode(3, ListNode(2, ListNode(0, ListNode(4))))
l1.nxt.nxt.nxt.nxt = l1.nxt
lc_test(1, hasCycle(l1), True)

l2 = ListNode(1, ListNode(2))
l2.nxt.nxt = l2
lc_test(2, hasCycle(l2), True)

l3 = ListNode(1)
lc_test(3, hasCycle(l3), False)
