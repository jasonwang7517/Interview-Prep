"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.
"""

class ConsecutiveCharacters(object):
    def maxPower(self, s):
        ans = 1
        current = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                if current > ans:
                    ans = current
                current = 1
        return max(current, ans)
            