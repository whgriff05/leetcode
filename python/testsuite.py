# Classes
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


# Helper functions
def list_to_linked_list(l):
    prev = None
    while l:
        prev = ListNode(l[-1], prev)
        del l[-1]

    return prev


# Test functions
def assert_eq(a, b):
    if isinstance(a, list) and isinstance(b, list):
        a.sort()
        b.sort()
    if a == b:
        return True
    else:
        return False

def lc_test(n, a, b):
    print(f"Test {n}: {'Passed' if assert_eq(a, b) else 'Failed'}")



