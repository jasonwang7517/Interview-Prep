"""
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned 
list must be sorted in increasing order.
"""

class FindTargetIndicesAfterSortingArray(object):
    def targetIndices(self, nums, target):
        nums.sort()
        ans = []
        for i in range(0, len(nums)):
            if nums[i] == target:
                ans.append(i)
            elif nums[i] > target:
                return ans
        return ans
        