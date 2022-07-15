"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
"""

class ThreeConsecutiveOdds(object):
    def threeConsecutiveOdds(self, arr):
        if len(arr) < 3:
            return False
        i = 0
        while i < len(arr) - 2:
            elem1 = arr[i]
            elem2 = arr[i + 1]
            elem3 = arr[i + 2]
            if elem1 % 2 == 1 and elem2 % 2 == 1 and elem3 % 2 == 1:
                return True
            i += 1
        return False
