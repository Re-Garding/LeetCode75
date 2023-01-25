"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'{self.val} {self.next}'

def reverseList(head):
# two pointers. one looks at where we are in the linked list, one looks at what came before that node,
# and we instantiate a temp pointer to look at the node that comes next on the original list. 
    prev, curr = None, head
    # to start, we are currently on the head, and nothing come before it

    while curr:
        forward = curr.next
        # lets make sure we know what came after the head/node we are looking at
        curr.next = prev
        # we want to 'reverse' the linked list pointer, so that the 'next' value is equal to what came
        # before
        prev = curr
        # we want to move our pointers.
        # our previous node is now where we just were sitting
        curr = forward
        # our current node is where the list went next
        print(prev)
    # we return previous because that is the variable we have been 'reversing' our pointers on
    # per line 40
    return prev




x = ListNode(1,ListNode(2,ListNode(3)))

print(reverseList(x))