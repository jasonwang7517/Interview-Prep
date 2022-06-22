"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, 
or return -1 otherwise.
"""

class LargestNumberAtLeastTwiceOfOthers(object):
    def dominantIndex(self, nums):
        if len(nums) == 1:
            return 0
        highest = max(nums)
        index = 0
        for i in range(len(nums)):
            if nums[i] == highest:
                index = i
                break
        nums.sort()
        if highest >= (2 * nums[-2]):
            return index
        return -1
        