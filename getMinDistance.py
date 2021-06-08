class Solution(object):
    def getMinDistance(self, nums, target, start):
        ans = float('inf')
        for i in range(0, len(nums)):
            if nums[i] == target:
                ans = min(abs(start - i), ans)
        return ans
