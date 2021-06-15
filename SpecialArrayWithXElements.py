"""
    You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are 
    greater than or equal to x.

    Notice that x does not have to be an element in nums.

    Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
"""

class SpecialArrayWithXElements(object):
    def specialArray(self, nums):
        nums.sort(reverse = True)
        i = 0
        while i < len(nums) and i < nums[i]:
            i += 1
        if i < len(nums) and i == nums[i]:
            return -1
        return i
        