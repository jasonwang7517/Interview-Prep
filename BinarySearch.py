"""
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
"""

class BinarySearch(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            curr = left + (right - left) // 2
            if nums[curr] == target:
                return curr
            if target < nums[curr]:
                right = curr - 1
            else:
                left = curr + 1
        return -1