"""
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.
"""

class NumberOfSegmentsInAString(object):
    def countSegments(self, s):
        return len(s.split())
        