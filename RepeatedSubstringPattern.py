"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
"""

class RepeatedSubstringPattern(object):
    def repeatedSubstringPattern(self, s):
        new_string = (s + s)[1:-1]
        return s in new_string