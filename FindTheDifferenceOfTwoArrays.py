"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
    - answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    - answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.
"""

class FindTheDifferenceOfTwoArrays(object):
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        diffs1 = []
        diffs2 = []
        for i in set1:
            if i not in set2:
                diffs1.append(i)
        for i in set2:
            if i not in set1:
                diffs2.append(i)
        return [diffs1, diffs2]
        