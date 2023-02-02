"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"N:{self.val}"

def lowestcommonancestor(root, p, q):
    cur = root

    while cur:

        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
            continue

        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
            continue
        else: return cur


a = TreeNode(5, TreeNode(4), TreeNode(6))
b = TreeNode(10, TreeNode(9), TreeNode(11))
c = TreeNode(8, a, b)
x = TreeNode(3, TreeNode(1), c)



lowestcommonancestor(x, TreeNode(9), TreeNode(11))
