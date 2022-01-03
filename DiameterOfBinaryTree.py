"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DiameterOfBinaryTree(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0
    
        def depth(p):
            if not p: 
                return 0
            left = depth(p.left)
            right = depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
            
        depth(root)
        return self.ans
        