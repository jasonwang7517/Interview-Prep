"""
    Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

    Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class NaryTreePreorderTraversal(object):
    def preorder(self, root):
        list = []
        if root == None:
            return list
        list.append(root.val)
        for el in root.children:
            list += self.preorder(el)
        return list
        