class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        index = len(nums) - 1
        while index >= 2:
            if nums[index] < nums[index - 1] + nums[index - 2]:
                return nums[index] + nums[index - 1] + nums[index - 2]
            index -= 1
        return 0
