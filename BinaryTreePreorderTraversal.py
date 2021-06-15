"""
    Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreePreorderTraversal(object):
    def preorderTraversal(self, root):
        ans = []
        if not root:
            return ans
        ans.append(root.val)
        ans.extend(self.preorderTraversal(root.left))
        ans.extend(self.preorderTraversal(root.right))
        return ans
