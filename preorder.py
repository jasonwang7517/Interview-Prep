"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        list = []
        if root == None:
            return list
        list.append(root.val)
        for el in root.children:
            list += self.preorder(el)
        return list
        