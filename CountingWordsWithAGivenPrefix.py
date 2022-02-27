"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
"""

class CountingWordsWithAGivenPrefix(object):
    def prefixCount(self, words, pref):
        length = len(pref)
        ans = 0
        for i in words:
            if len(i) <= pref and i[:length] == pref:
                ans += 1
        return ans
        