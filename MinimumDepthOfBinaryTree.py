"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class MinimumDepthOfBinaryTree(object):
    def minDepth(self, root):
        if root is None:
            return 0
        return self.traverse(root)
        
    def traverse(self, root):
        if root is None:
            return float('inf')
        if root.left is None and root.right is None:
            return 1
        return 1 + min(self.traverse(root.left), self.traverse(root.right))