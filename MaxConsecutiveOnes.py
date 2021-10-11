"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class MaxConsecutiveOnes(object):
    def findMaxConsecutiveOnes(self, nums):
        ans = 0
        current_streak = 0
        for i in nums:
            if i == 1:
                current_streak += 1
            else:
                if current_streak > ans:
                    ans = current_streak
                current_streak = 0
        return max(current_streak, ans)
        