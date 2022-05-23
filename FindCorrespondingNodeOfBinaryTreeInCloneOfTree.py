"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindCorrespondingNodeOfBinaryTreeInCloneOfTree(object):
    def getTargetCopy(self, original, cloned, target):
        q = []
        q.append(cloned)
        while len(q) > 0:
            current = q.pop()
            if current.val == target.val:
                return current
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
