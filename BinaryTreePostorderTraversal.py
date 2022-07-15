"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BinaryTreePostorderTraversal(object):
    def postorderTraversal(self, root):
        ans = []
        if not root:
            return ans
        else:
            ans.extend(self.postorderTraversal(root.left))
            ans.extend(self.postorderTraversal(root.right))
            ans.append(root.val)
            return ans
        