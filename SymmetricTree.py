"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class SymmetricTree(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.is_mirrored(root.left, root.right)
        
    def is_mirrored(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        if left.val == right.val:
            outside = self.is_mirrored(left.left, right.right)
            inside = self.is_mirrored(left.right, right.left)
            return outside and inside
        return False
