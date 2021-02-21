class Solution(object):
    def findLucky(self, arr):
        freqs = [0] * 501
        for i in arr:
            freqs[i] += 1
        for i in range(len(freqs) - 1, 0, -1):
            if freqs[i] == i:
                return i
        return -1
