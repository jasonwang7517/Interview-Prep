"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
"""

class KthDistinctStringInArray(object):
    def kthDistinct(self, arr, k):
        counts = {}
        for i in arr:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        index = 1
        for i in arr:
            if counts[i] == 1:
                if index == k:
                    return i
                index += 1
        return ""