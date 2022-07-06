"""
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
"""

class FindSubsequenceOfLengthKWithLargestSum(object):
    def maxSubsequence(self, nums, k):
        ans = nums[:k]
        min_val = min(ans)
        index = k
        while index < len(nums):
            if nums[index] > min_val:
                ans.remove(min_val)
                ans.append(nums[index])
                min_val = min(ans)
            index += 1
        return ans
        