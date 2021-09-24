"""
    Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

    The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""

class FindGreatestCommonDivisor(object):
    def findGCD(self, nums):
        minVal = min(nums)
        maxVal = max(nums)
        while minVal:
            minVal, maxVal = maxVal % minVal, minVal
        return maxVal