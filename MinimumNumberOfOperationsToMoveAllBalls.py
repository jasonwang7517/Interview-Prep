"""
    You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

    In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more 
    than one ball in some boxes.

    Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

    Each answer[i] is calculated considering the initial state of the boxes.
"""

class MinimumNumberOfOperationsToMoveAllBalls(object):
    def minOperations(self, boxes):
        ans = [0 for i in range(len(boxes))]
        for i in range(0, len(ans) - 1):
            moves = 0
            for j in range(i + 1, len(ans)):
                if boxes[j] == '1':
                    moves += j - i
            ans[i] += moves
        for k in range(len(ans) - 1, 0, -1):
            moves = 0
            for l in range(k - 1, -1, -1):
                if boxes[l] == '1':
                    moves += abs(k - l)
            ans[k] += moves
        return ans
        