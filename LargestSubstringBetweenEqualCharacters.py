"""
    Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

    A substring is a contiguous sequence of characters within a string.
"""

class LargestSubstringBetweenEqualCharacters(object):
    def maxLengthBetweenEqualCharacters(self, s):
        ans = -1
        seen = {}
        for i in range(0, len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
            else:
                ans = max(ans, i - seen[s[i]] - 1)
        return ans