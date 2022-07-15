"""
Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. 

A pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.
"""

class DetectPatternOfLengthM(object):
    def containsPattern(self, arr, m, k):
        left_index = 0
        while left_index <= len(arr) - 1:
            window = arr[left_index : left_index + m]
            if window * k == arr[left_index : left_index + (m * k)]:
                return True
            left_index += 1
        return False
        