"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""

class MinimumValueToGetPositiveStepByStepSum(object):
    def minStartValue(self, nums):
        runSum = 0
        lowestSoFar = 1
        for i in nums:
            runSum += i
            if runSum < lowestSoFar:
                lowestSoFar = runSum
        return max(1, 1 + (lowestSoFar * -1))