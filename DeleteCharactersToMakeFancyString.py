"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.
"""

class DeleteCharactersMakeFancyString(object):
    def makeFancyString(self, s):
        count = 0
        chars = []
        for i, c in enumerate(s):
            if i > 0 and c == s[i - 1]:    
                count += 1    
            else:
                count = 1
            if count < 3:
                chars.append(c)
        return ''.join(chars)