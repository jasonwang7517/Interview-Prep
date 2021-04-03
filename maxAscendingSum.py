class Solution(object):
    def maxAscendingSum(self, nums):
        maximum = nums[0]
        currVal = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                currVal += nums[i]
            else:
                if currVal > maximum:
                    maximum = currVal
                currVal = nums[i]
        return max(currVal, maximum)
