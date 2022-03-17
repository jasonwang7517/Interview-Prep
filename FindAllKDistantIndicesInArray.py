"""
You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.
"""

class FindAllKDistantIndicesInArray(object):
    def findKDistantIndices(self, nums, key, k):
        indices = []
        ans = []
        for i in range(len(nums)):
            if nums[i] == key:
                indices.append(i)
        for i in range(len(nums)):
            for j in indices:
                if abs(i - j) <= k:
                    ans.append(i)
                    break
        return ans
        