"""
    Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any 
    triangle of a non-zero area, return 0.
"""

class LargestPerimeterTriangle(object):
    def largestPerimeter(self, nums):
        nums.sort()
        index = len(nums) - 1
        while index >= 2:
            if nums[index] < nums[index - 1] + nums[index - 2]:
                return nums[index] + nums[index - 1] + nums[index - 2]
            index -= 1
        return 0
