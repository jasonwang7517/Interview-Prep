"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class MinimumAbsoluteDifferenceInBST(object):
    
    ans = float('inf')
    prev = None
    
    def getMinimumDifference(self, root):
        if root is None:
            return self.ans
        self.getMinimumDifference(root.left)
        if self.prev is not None:
            self.ans = min(self.ans, root.val - self.prev)
        self.prev = root.val
        self.getMinimumDifference(root.right)
        return self.ans
