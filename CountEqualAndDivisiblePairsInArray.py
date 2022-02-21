"""
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k. 
"""

class CountEqualAndDivisiblePairsInArray(object):
    def countPairs(self, nums, k):
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                current_tuple = (nums[i], nums[j])
                if nums[i] == nums[j] and (i * j) % k == 0:
                    ans += 1
        return ans
        