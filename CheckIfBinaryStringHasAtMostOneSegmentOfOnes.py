"""
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.
"""

class Solution(object):
    def checkOnesSegment(self, s):
        contiguous = False
        total_segs = 0
        for i in s:
            if i == '1' and not contiguous:
                total_segs += 1
                contiguous = True
            if i == '0' and contiguous:
                contiguous = False
        return total_segs <= 1