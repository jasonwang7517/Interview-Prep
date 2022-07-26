"""
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:
    - A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
    - s will contain at least one letter that appears twice.
"""

class FirstLetterToAppearTwice(object):
    def repeatedCharacter(self, s):
        seen = set()
        for i in s:
            if i in seen:
                return i
            seen.add(i)