"""
Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.
"""

class CountElementsWithStrictlySmallerAndGreaterElements(object):
    def countElements(self, nums):
        nums.sort()
        left_pointer = 0
        while left_pointer < len(nums) and nums[left_pointer] == nums[0]:
            left_pointer += 1
        right_pointer = len(nums) - 1
        while nums[right_pointer] == nums[len(nums) - 1] and right_pointer >= 0:
            right_pointer -= 1
        return max(0, right_pointer - left_pointer + 1)
        