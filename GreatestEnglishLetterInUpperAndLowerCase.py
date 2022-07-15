"""
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. 

The returned letter should be in uppercase. 

If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.
"""

class GreatestEnglishLetterInUpperAndLowerCase(object):
    def greatestLetter(self, s):
        chars = set()
        for i in s:
            chars.add(i)
        for i in range(91, 64, -1):
            if chr(i) in chars and chr(i + 32) in chars:
                return chr(i)
        return ""