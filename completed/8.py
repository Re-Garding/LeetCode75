"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __repr__(self):
    #     return f'{self.val} {self.next}'
    def add_next(self, nex):
        self.next = nex


x = ListNode(3)
y = ListNode(2)
z = ListNode(0)
a = ListNode(4)

x.add_next(y)
y.add_next(z)
z.add_next(a)
a.add_next(y)


def detectCycle(head):
    location = {}
    count = 0
    while head:
        if head in location:
            return head
        else:
            location[head] = count
        count += 1
        head = head.next


print(detectCycle(x))