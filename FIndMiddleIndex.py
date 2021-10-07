"""
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.
"""

class FindMiddleIndex(object):
    def findMiddleIndex(self, nums):
        total_sum = sum(nums)
        cumulative_sum = 0
        for i in range(len(nums)):
            curr_sum = total_sum - nums[i]
            if cumulative_sum == curr_sum / 2 and curr_sum % 2 == 0:
                return i
            cumulative_sum += nums[i]
        return -1
        
        