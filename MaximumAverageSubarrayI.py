"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

class MaximumAverageSubarrayI(object):
    def findMaxAverage(self, nums, k):
        index = k
        window = nums[:k]
        current_max = sum(window)
        current_sum = current_max
        while index < len(nums):
            current_sum -= window.pop(0)
            window.append(nums[index])
            current_sum += nums[index]
            current_max = max(current_max, current_sum)
            index += 1
        return current_max / 1.0 / k 
        