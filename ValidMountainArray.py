"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

class ValidMountainArray(object):
    def validMountainArray(self, arr):
        increased = 0
        decreased = 0
        index = 1
        while index < len(arr):
            if arr[index] == arr[index - 1]:
                return False
            if arr[index] < arr[index - 1]:
                index += 1
                decreased += 1
                break
            else:
                increased += 1
                index += 1
        while index < len(arr):
            if arr[index] >= arr[index - 1]:
                return False
            else:
                index += 1
                decreased += 1
        return decreased >= 1 and increased >= 1 