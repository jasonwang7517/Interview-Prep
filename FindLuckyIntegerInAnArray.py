"""
    Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

    Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
"""

class FindLuckyIntegerInAnArray(object):
    def findLucky(self, arr):
        freqs = [0] * 501
        for i in arr:
            freqs[i] += 1
        for i in range(len(freqs) - 1, 0, -1):
            if freqs[i] == i:
                return i
        return -1
