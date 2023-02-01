"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'{self.val} {self.next}'


def middleNode(head):
    count = 0
    counting = head
    while counting:
        count += 1
        counting = counting.next
    middle = (count//2)
    count = 0
    while count < middle:
        count += 1
        head = head.next
    return head









x = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))

print(middleNode(x))