"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to 
itself.
"""

class IsomorphicString(object):
    def isIsomorphic(self, s, t):
        dictionary = {}
        for i in range(len(s)):
            if s[i] not in dictionary:
                dictionary[s[i]] = t[i]
            if s[i] in dictionary and t[i] != dictionary[s[i]]:
                return False
        dictionary = {}
        for i in range(len(t)):
            if t[i] not in dictionary:
                dictionary[t[i]] = s[i]
            if t[i] in dictionary and s[i] != dictionary[t[i]]:
                return False
        return True
        