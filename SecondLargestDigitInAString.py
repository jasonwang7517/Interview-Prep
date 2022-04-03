"""
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.
"""

class Solution(object):
    def secondHighest(self, s):
        digits = set()
        for i in s:
            if i <= '9' and i >= '0':
                digits.add(i)
        if len(digits) < 2:
            return -1
        return sorted(digits)[-2]