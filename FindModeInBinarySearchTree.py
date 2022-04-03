"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    - The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    - Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution(object):
    def findMode(self, root):
        counts = defaultdict(lambda: 0)
        self.traverse(root, counts)
        curr_max = max(counts.values())
        ans = []
        for i in counts:
            if counts[i] == curr_max:
                ans.append(i)
        return ans
            
    def traverse(self, root, dic):
        if root:
            dic[root.val] += 1
            self.traverse(root.left, dic)
            self.traverse(root.right, dic)
        return dic
        