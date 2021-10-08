"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
from collections import defaultdict

class FirstUniqueCharacter(object):
    def firstUniqChar(self, s):
        letter_counts = defaultdict(int)
        for i in s:
            letter_counts[i] += 1
        for i in range(len(s)):
            if letter_counts[s[i]] == 1:
                return i
        return -1
        