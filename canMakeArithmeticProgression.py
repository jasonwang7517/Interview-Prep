"""
    A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

    Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
"""

class CanMakeArithmeticProgression(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        if len(arr) == 2:
            return True
        else:
            diff = arr[1] - arr[0]
            for i in range (2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True