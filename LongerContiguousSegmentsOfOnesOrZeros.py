"""
    Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.
    - For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
    
    Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.
"""

class LongerContiguousSegmentsOfOnesOrZeros(object):
    def checkZeroOnes(self, s):
        longest1s = 0
        curr1s = 0
        longest0s = 0
        curr0s = 0
        for i in s:
            if i == '0':
                if curr1s == 0:
                    curr0s += 1
                elif curr1s > 0:
                    longest1s = max(longest1s, curr1s)
                    curr1s = 0
                    curr0s = 1
            elif i == '1':
                if curr0s == 0:
                    curr1s += 1
                elif curr0s > 0:
                    longest0s = max(longest0s, curr0s)
                    curr0s = 0
                    curr1s = 1
        longest1s = max(longest1s, curr1s)
        longest0s = max(longest0s, curr0s)
        return longest1s > longest0s
