"""
    Given the root of a binary tree, invert the tree, and return its root.
"""

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class InvertBinaryTree(object):
    def invertTree(self, root):
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root
        elif root.left is None and root.right is not None:
            root.left = self.invertTree(root.right)
            root.right = None
            return root
        elif root.left is not None and root.right is None:
            root.right = self.invertTree(root.left)
            root.left = None
            return root
        else:
            newLeft = self.invertTree(root.right)
            newRight = self.invertTree(root.left)
            root.left = newLeft
            root.right = newRight
            return root