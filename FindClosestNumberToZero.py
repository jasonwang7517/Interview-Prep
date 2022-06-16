"""
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.
"""

class FindClosestNumber(object):
    def findClosestNumber(self, nums):
        ans = nums[0]
        min_dist = abs(ans)
        for i in nums:
            if i == 0:
                return 0
            if (abs(i) == min_dist and i > ans) or abs(i) < min_dist:
                min_dist = abs(i)
                ans = i
        return ans
        