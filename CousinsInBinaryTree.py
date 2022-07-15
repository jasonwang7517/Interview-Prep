"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and 
y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class CousinsInBinaryTree(object):
    def isCousins(self, root, x, y):
        def dfs(node, depth):
            for child in (node.left, node.right):
                if child:
                    if child.val in (x, y): 
                        parent[child.val] = depth, node.val
                    dfs(child, depth + 1)        
                        
        parent = {}
        dfs(root, 0)
        X, Y = parent.get(x, (-1, -1)), parent.get(y, (-2, -2))
        return X[0] == Y[0] and X[1] != Y[1]
        
        