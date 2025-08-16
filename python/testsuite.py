# Classes
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        return f"<ListNode ({self.val}) -> {self.nxt}>"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<TreeNode ({self.val}) -> [{self.left.val if self.left else 'None'}, {self.right.val if self.right else 'None'}]>"

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        output = f"<Node ({self.val}) -> ["
        if self.children:
            for i in range(len(self.children) - 1):
                output += f"{self.children[i].val if self.children[i] else 'None'}, "
            output += f"{self.children[-1].val if self.children[-1] else 'None'}"
        output += "]>"
        return output
        
        

# Helper functions
def list_to_linked_list(l):
    prev = None
    while l:
        prev = ListNode(l[-1], prev)
        del l[-1]

    return prev

def print_linked_list(l):
    curr = l
    while curr != None:
        print(curr.val, end=" ")
        curr = curr.nxt
    print(" ")


# Test functions
def assert_eq(a, b):
    # Comparing Linked Lists
    if isinstance(a, ListNode) and isinstance(b, ListNode):
        alist = []
        blist = []
        while a != None:
            alist.append(a.val)
            a = a.nxt

        while b != None:
            blist.append(b.val)
            b = b.nxt

        a = alist
        b = blist

    '''Confused why this was here
    # Comparing Lists
    if isinstance(a, list) and isinstance(b, list):
        a.sort()
        b.sort()
    '''

        
    if a == b:
        return True
    else:
        return False

def lc_test(n, a, b):
    if assert_eq(a, b):
        print(f"Test {n}: Passed")
    else:
        print(f"Test {n}: Failed | Expected {b}, received {a}")



