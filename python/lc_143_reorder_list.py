from testsuite import ListNode

def reorderList(head):
    def revList(head):
        prev = None
        curr = head

        while curr:
            nxt = curr.nxt
            curr.nxt = prev
            prev = curr
            curr = nxt

        return prev


    if not head: return
    if not head.nxt: return

    fast = head
    slow = head

    while fast and fast.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt

    one_behind_slow = head
    while one_behind_slow.nxt != slow:
        one_behind_slow = one_behind_slow.nxt

    one_behind_slow.nxt = None

    slow = revList(slow)

    hp = head
    while head and slow:
        nxt = head.nxt # get next head
        slow_insert = slow # get slow to insert
        slow = slow.nxt # move slow forward

        head.nxt = slow_insert # insert slow_insert
        slow_insert.nxt = nxt # insert slow_insert
        head = nxt # move head forward

    head = hp
    while head.nxt:
        head = head.nxt

    head.nxt = slow

# Tests
from testsuite import lc_test

h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
lc_test(1, reorderList(h1), ListNode(1, ListNode(4, ListNode(2, ListNode(3)))))

h2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
lc_test(2, reorderList(h2), ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3))))))

