"""
    You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

    At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

    An integer x - Record a new score of x.
    - "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
    - "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
    - "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
    
    Return the sum of all the scores on the record.
"""

class BaseballGame(object):
    def calPoints(self, ops):
        scores = []
        runningSum = 0
        for i in ops:
            if i == "C":
                runningSum -= int(scores[-1])
                del scores[-1]
            elif i == "D":
                runningSum += 2 * int(scores[-1])
                scores.append(str(2 * int(scores[-1])))
            elif i == "+":
                lastTwoSum = int(scores[-1]) + int(scores[-2])
                scores.append(str(lastTwoSum))
                runningSum += lastTwoSum
            else:
                scores.append(i)
                runningSum += int(i)
        return runningSum
