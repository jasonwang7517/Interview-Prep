"""
    You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and 
    swap the characters at these indices.

    Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
"""

class CheckIfOneStringSwapCanMakeStringsEqual(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        diffs = []
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
        if len(diffs) > 2:
            return False
        return len(diffs) == 0 or (len(diffs) == 2 and s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]])