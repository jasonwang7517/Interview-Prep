"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then 
this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class SecondMinimumNodeInABinaryTree(object):
    def findSecondMinimumValue(self, root):
        vals = set()
        q = []
        q.append(root)
        while len(q) > 0:
            current = q.pop(0)
            if current.left is None and current.right is None:
                vals.add(current.val)
            else:
                vals.add(min(current.left.val, current.right.val))
                q.append(current.left)
                q.append(current.right)
        if len(vals) <= 1:
            return -1
        ans = list(vals)
        ans.sort()
        return ans[1]
        