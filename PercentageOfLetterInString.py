"""
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.
"""

from math import floor

class PercentageOfLetterInString(object):
    def percentageLetter(self, s, letter):
        counts = 0
        for i in s:
            if i == letter:
                counts += 1
        return int(floor(100 * counts / len(s)))
        