"""
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.
"""

class CheckIfAll1sAreAtLeastKPlacesAway(object):
    def kLengthApart(self, nums, k):
        spaces = 0
        index = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                index = i
                break
        lastIndex = index
        for i in range(index + 1, len(nums)):
            diff = i - lastIndex - 1
            if nums[i] == 1 and diff < k:
                return False
            if nums[i] == 1:
                lastIndex = i
        return True