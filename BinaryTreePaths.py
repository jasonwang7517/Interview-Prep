"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BinaryTreePaths(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
        return res