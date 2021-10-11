"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
"""

class KthMissingPositiveNumber(object):
    def findKthPositive(self, arr, k):
        missing = []
        current_value = 1
        arr_index = 0
        while arr_index < len(arr):
            if arr[arr_index] > current_value:
                if len(missing) == k - 1:
                    return current_value
                missing.append(current_value)
            elif arr[arr_index] == current_value:
                arr_index += 1
            current_value += 1
        while len(missing) < k:
            missing.append(current_value)
            current_value += 1
        return missing[-1]
                
        