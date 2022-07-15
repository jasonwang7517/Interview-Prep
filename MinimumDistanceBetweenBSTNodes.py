"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class MinimumDistanceBetweenBSTNodes(object):
    def minDiffInBST(self, root):
        elements = self.inOrder(root)
        elements.sort()
        ans = float('inf')
        for i in range(0, len(elements) - 1):
            if elements[i + 1] - elements[i] < ans:
                ans = elements[i + 1] - elements[i]
        return ans                
            
    def inOrder(self, root):
        values = []
        if root:
            values.append(root.val)
            values.extend(self.inOrder(root.left))
            values.extend(self.inOrder(root.right))
        return values
        