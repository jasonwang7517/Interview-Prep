class Solution(object):
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
