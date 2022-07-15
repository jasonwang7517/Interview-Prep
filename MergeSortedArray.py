"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class MergeSortedArray(object):
    def merge(self, nums1, m, nums2, n):
        index = len(nums1) - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            elif nums2[n] >= nums1[m]:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1
        if n >= 0:
            while index >= 0:
                nums1[index] = nums2[n]
                n -= 1
                index -= 1