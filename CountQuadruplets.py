"""
Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

nums[a] + nums[b] + nums[c] == nums[d], and a < b < c < d
"""
from collections import defaultdict

class CountQuadruplets(object):
    def countQuadruplets(self, nums):
        ans = 0
        
        count = defaultdict(int)
        count[nums[len(nums)-1] - nums[len(nums)-2]] = 1
        
        for i in range(len(nums) - 3, 0, -1):
            for j in range(i - 1, -1, -1):
                ans += count[nums[i] + nums[j]]
            
            for k in range(len(nums) - 1, i, -1):
                count[nums[k] - nums[i]] += 1
        return ans
        