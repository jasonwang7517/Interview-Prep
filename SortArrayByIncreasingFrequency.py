"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing 
order.

Return the sorted array.
"""

from typing import Collection

class SortArrayByIncreasingFrequency(object):
    def frequencySort(self, nums):
        cnt = Collection.Counter(nums)
        return sorted(nums, key = lambda n: (cnt[n], -n))
        
        