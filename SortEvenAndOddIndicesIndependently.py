"""
You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:

    Sort the values at odd indices of nums in non-increasing order.
        For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
    Sort the values at even indices of nums in non-decreasing order.
        For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.

Return the array formed after rearranging the values of nums.
"""

class SortEvenOddIndicesIndependently(object):
    def sortEvenOdd(self, nums):
        odd_indices = []
        even_indices = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even_indices.append(nums[i])
            else:
                odd_indices.append(nums[i])
        odd_indices.sort(reverse=True)
        even_indices.sort()
        ans = []
        while len(odd_indices) > 0 and len(even_indices) > 0:
            ans.append(even_indices.pop(0))
            ans.append(odd_indices.pop(0))
        if len(even_indices) > 0:
            ans.append(even_indices.pop(0))
        return ans
        