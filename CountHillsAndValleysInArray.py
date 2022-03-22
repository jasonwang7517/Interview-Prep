"""
You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.
"""

class CountHillsAndValleysInArray(object):
    def countHillValley(self, nums):
        ans = 0
        index = 1
        while index < len(nums) - 1:
            left_index = index - 1
            while nums[left_index] == nums[index] and left_index > 0:
                left_index -= 1
            right_index = index + 1
            while nums[right_index] == nums[index] and right_index < len(nums) - 1:
                right_index += 1
            if (nums[index] > nums[left_index] and nums[index] > nums[right_index]) or (nums[index] < nums[left_index] and nums[index] < nums[right_index]):
                ans += 1
            index = right_index
        return ans