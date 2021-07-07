"""
    An array is monotonic if it is either monotone increasing or monotone decreasing.

    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].  An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

    Return true if and only if the given array nums is monotonic.
"""

class MonotonicArray(object):
    def isMonotonic(self, nums):
        if len(nums) == 1:
            return True
        index = 1
        while index < len(nums) and nums[index] == nums[index - 1]:
            index += 1
        if index >= len(nums):
            return True
        if nums[index] > nums[index - 1]:
            for i in range(index, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
        elif nums[index] < nums[index - 1]:
            for i in range(index, len(nums)):
                if nums[i] > nums[i - 1]:
                    return False
        return True
        