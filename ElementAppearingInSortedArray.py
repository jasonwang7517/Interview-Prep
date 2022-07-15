"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
"""

class ElementAppearingInSortedArray(object):
    def findSpecialInteger(self, arr):
        toBeat = len(arr) // 4
        for i in range(0, len(arr) - toBeat):
            if arr[i] == arr[i + toBeat]:
                return arr[i]