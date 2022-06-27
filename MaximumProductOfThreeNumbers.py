"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""

class MaximumProductOfThreeNumbers(object):
    def maximumProduct(self, nums):
        min_1 = float('inf')
        min_2 = float('inf')
        max_1 = -float('inf')
        max_2 = -float('inf')
        max_3 = -float('inf')
        for i in nums:
            if i <= min_1:
                min_2 = min_1
                min_1 = i
            elif i <= min_2:
                min_2 = i
            if i >= max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = i
            elif i >= max_2:
                max_3 = max_2
                max_2 = i
            elif i >= max_3:
                max_3 = i
        return max(min_1 * min_2 * max_1, max_1 * max_2 * max_3)
