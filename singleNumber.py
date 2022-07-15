"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class SingleNumber(object):
    def singleNumber(self, nums):
        lastNum = set()
        for i in nums:
            if i not in lastNum:
                lastNum.add(i)
            elif i in lastNum:
                lastNum.remove(i)
        for i in lastNum:
            return i
