from testsuite import ListNode, print_linked_list

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.nxt = list1
            list1 = list1.nxt
        else:
            tail.nxt = list2
            list2 = list2.nxt
        tail = tail.nxt

    if list1:
        tail.nxt = list1
    else:
        tail.nxt = list2

    return dummy.nxt

    

# Tests
from testsuite import lc_test, list_to_linked_list
lc_test(1, mergeTwoLists(list_to_linked_list([1, 2, 4]), list_to_linked_list([1, 3, 4])), list_to_linked_list([1, 1, 2, 3, 4, 4]))
lc_test(2, mergeTwoLists(list_to_linked_list([]), list_to_linked_list([])), list_to_linked_list([]))
lc_test(3, mergeTwoLists(list_to_linked_list([]), list_to_linked_list([0])), list_to_linked_list([0]))
