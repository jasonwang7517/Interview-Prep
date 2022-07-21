"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
"""

class ThirdMaximumNumber(object):
    def thirdMax(self, nums):
        new_nums = list(set(nums))
        if len(new_nums) < 3:
            return max(new_nums)
        new_nums.sort()
        return new_nums[-3]