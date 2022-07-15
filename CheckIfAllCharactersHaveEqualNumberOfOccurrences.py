"""
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
"""

class CheckIfAllCharactersHaveEqualNumberOfOccurrences(object):
    def areOccurrencesEqual(self, s):
        counts = {}
        last = 0
        for i in s:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
            last = counts[i]
        for i in counts:
            if counts[i] != last:
                return False
        return True