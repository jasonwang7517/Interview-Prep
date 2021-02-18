class Solution(object):
    def minStartValue(self, nums):
        runSum = 0
        lowestSoFar = 1
        for i in nums:
            runSum += i
            if runSum < lowestSoFar:
                lowestSoFar = runSum
        return max(1, 1 + (lowestSoFar * -1))