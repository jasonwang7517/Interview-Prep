"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the 
path equals targetSum.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class PathSum(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
        