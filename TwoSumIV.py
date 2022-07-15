"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TwoSumIV(object):
    def findTarget(self, root, k):
        sums = {}
        q = []
        q.append(root)
        while (q):
            curr = q.pop(0)
            if (k - curr.val) in sums:
                return True
            sums[curr.val] = k - curr.val
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False
            
        