from testsuite import ListNode, print_linked_list

def reverseList(head):
    current = head
    prev = None
    
    while current != None:
        prev = ListNode(current.val, prev)
        current = current.nxt


    return prev


# Tests
from testsuite import lc_test, list_to_linked_list
lc_test(1, reverseList(list_to_linked_list([1,2,3,4,5])), list_to_linked_list([5,4,3,2,1]))
lc_test(2, reverseList(list_to_linked_list([1,2])), list_to_linked_list([2,1]))
lc_test(3, reverseList(list_to_linked_list([])), list_to_linked_list([]))
