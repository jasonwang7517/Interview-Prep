"""
    A string is good if there are no repeated characters.

    Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

    Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

    A substring is a contiguous sequence of characters in a string.
"""

class SubstringsOfSizeThreeWithDistinctCharacters(object):
    def countGoodSubstrings(self, s):
        ans = 0
        for i in range(0, len(s) - 2):
            currStr = set(s[i:i + 3])
            if len(currStr) == 3:
                ans += 1
        return ans
