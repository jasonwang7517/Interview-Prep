"""
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for i in letters:
            if i > target:
                return i
        return letters[0]