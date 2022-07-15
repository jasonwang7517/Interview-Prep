"""
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""

class TwoSumII(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        currSum = numbers[left] + numbers[right]
        while currSum != target:
            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            currSum = numbers[left] + numbers[right]
        return [left + 1, right + 1]
        