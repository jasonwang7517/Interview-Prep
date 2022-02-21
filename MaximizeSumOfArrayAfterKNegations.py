"""
Given an integer array nums and an integer k, modify the array in the following way:
    - Choose an index i and replace nums[i] with -nums[i].

You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.
"""

class MaximizeSumOfArrayAfterKNegations(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        index = 0
        while index < len(nums) and nums[index] < 0 and k > 0:
            nums[index] *= -1
            k -= 1
            index += 1
        if k % 2 == 0:
            return sum(nums)
        else:
            return sum(nums) - (2 * min(nums))
