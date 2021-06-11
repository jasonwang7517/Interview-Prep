"""
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append 
    the additional letters onto the end of the merged string.

    Return the merged string.
"""

class MergeStringsAlternately(object):
    def mergeAlternately(self, word1, word2):
        word1Index = 0
        word2Index = 0
        ans = ""
        while word1Index < len(word1) and word2Index < len(word2):
            ans += word1[word1Index]
            ans += word2[word2Index]
            word1Index += 1
            word2Index += 1
        if word1Index >= len(word1) and word2Index < len(word2):
            ans += word2[word2Index:]
        elif word2Index >= len(word2) and word1Index < len(word1):
            ans += word1[word1Index:]
        return ans