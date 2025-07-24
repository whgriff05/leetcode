from testsuite import ListNode, print_linked_list

def rotateRight(head, k):
    if head == None or head.nxt == None:
        return head
    
    curr = head
    counter = 1
    while curr.nxt != None:
        curr = curr.nxt
        counter += 1
    curr.nxt = head

    curr = head
    if k >= counter:
        k = k % counter
    
    for i in range(counter - k - 1):
        curr = curr.nxt

    new_head = curr.nxt
    curr.nxt = None

    return new_head

    

# Tests
from testsuite import lc_test, list_to_linked_list
lc_test(1, rotateRight(list_to_linked_list([1, 2, 3, 4, 5]), 2), list_to_linked_list([4, 5, 1, 2, 3]))
lc_test(2, rotateRight(list_to_linked_list([0, 1, 2]), 4), list_to_linked_list([2, 0, 1]))
lc_test(3, rotateRight(list_to_linked_list([]), 0), list_to_linked_list([]))
lc_test(4, rotateRight(list_to_linked_list([1, 2]), 2), list_to_linked_list([1, 2]))

