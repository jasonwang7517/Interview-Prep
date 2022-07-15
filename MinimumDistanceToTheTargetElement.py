"""
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that 
abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.
"""

class MinimumDistanceToTheTargetElement(object):
    def getMinDistance(self, nums, target, start):
        ans = float('inf')
        for i in range(0, len(nums)):
            if nums[i] == target:
                ans = min(abs(start - i), ans)
        return ans
