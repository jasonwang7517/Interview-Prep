"""
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.
"""

class NumberOfStringsThatAreSubstringsOfWord(object):
    def numOfStrings(self, patterns, word):
        ans = 0
        for i in patterns:
            if i in word:
                ans += 1
        return ans