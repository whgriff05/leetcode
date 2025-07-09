from testsuite import ListNode

def addTwoNumbers(l1, l2):
    l1_num = 0
    l2_num = 0

    curr = l1
    mult = 0
    while curr:
        l1_num += (curr.val * (10**mult))
        curr = curr.nxt
        mult += 1


    curr = l2
    mult = 0
    while curr:
        l2_num += (curr.val * (10**mult))
        curr = curr.nxt
        mult += 1

    s = list(map(int, str(l1_num + l2_num)))
    s.reverse()

    prev = None
    while s:
        prev = ListNode(s[-1], prev)
        del s[-1]

    return prev
    

# Tests
from testsuite import lc_test, list_to_linked_list
lc_test(1, addTwoNumbers(list_to_linked_list([2, 4, 3]), list_to_linked_list([5, 6, 4])), list_to_linked_list([7, 0, 8]))
lc_test(2, addTwoNumbers(list_to_linked_list([0]), list_to_linked_list([0])), list_to_linked_list([0]))
lc_test(3, addTwoNumbers(list_to_linked_list([9, 9, 9, 9, 9, 9, 9]), list_to_linked_list([9, 9, 9, 9])), list_to_linked_list([8, 9, 9, 9, 0, 0, 0, 1]))

