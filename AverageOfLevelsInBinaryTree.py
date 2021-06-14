"""
    Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class AverageOfLevelsInBinaryTree(object):
    def averageOfLevels(self, root):
        ans = []
        q = []
        q.append(root)

        while len(q) > 0:
            currSum = 0
            length = len(q)
            for i in range(0, length):
                temp = q.pop(0)
                currSum += temp.val
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            average = 1.0 * currSum / length
            ans.append(average)
        return ans
