from testsuite import ListNode, print_linked_list

def removeNthFromList(head, n):
    current = head
    prev = None
    
    while current != None:
        prev = ListNode(current.val, prev)
        current = current.nxt
    head = prev

    if n == 1:
        head = head.nxt
    else:
        previous = head
        for i in range(n - 2):
            previous = previous.nxt

        previous.nxt = previous.nxt.nxt
    


    current = head
    prev = None
    
    while current != None:
        prev = ListNode(current.val, prev)
        current = current.nxt
    head = prev


    return head
    


# Tests
from testsuite import lc_test, list_to_linked_list
lc_test(1, removeNthFromList(list_to_linked_list([1, 2, 3, 4, 5]), 2), list_to_linked_list([1, 2, 3, 5]))
lc_test(2, removeNthFromList(list_to_linked_list([1]), 1), None)
lc_test(3, removeNthFromList(list_to_linked_list([1, 2]), 1), list_to_linked_list([1]))
