"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class MajorityElement(object):
    def majorityElement(self, nums):
        currCount = 0
        currCandidate = None
        for i in nums:
            if currCount == 0:
                currCandidate = i
            if i == currCandidate:
                currCount += 1
            else:
                currCount -= 1
        return currCandidate