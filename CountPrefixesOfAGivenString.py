"""
You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.

Return the number of strings in words that are a prefix of s.

A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.
"""

class CountPrefixesOfAGivenString(object):
    def countPrefixes(self, words, s):
        ans = 0
        for i in words:
            end_bound = len(i)
            if len(s) >= end_bound and i in s[:end_bound]:
                print(i)
                print(s[:end_bound])
                ans += 1
        return ans
        