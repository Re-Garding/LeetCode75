"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} L:{self.left} R:{self.right}"

a = TreeNode(4, TreeNode(3), TreeNode(6))
b = TreeNode(5, TreeNode(1), a)

c = TreeNode(1, TreeNode(None), TreeNode(1))

def isValid(root):


    def valid(node, left, right):
        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False
        return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

    return valid(root, float("-inf"), float("inf"))


print(isValid(c))
