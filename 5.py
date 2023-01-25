"""

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'{self.val} {self.next}'

def mergeTwoLists(list1, list2):

    if list1 == [] and list2 == []:
        return []
    elif list1 == []:
        return list2
    elif list2 == []:
        return list1

    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    return dummy.next




x = ListNode(1,ListNode(2,ListNode(4)))
y = ListNode(1,ListNode(3,ListNode(4)))

m = None
b = None
print(mergeTwoLists(x,y))