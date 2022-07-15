"""
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. 

That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
"""

class ReformatTheString(object):
    def reformat(self, s):
        characters = []
        digits = []
        for i in s:
            if i >= 'a' and i <= 'z':
                characters.append(i)
            else:
                digits.append(i)
        ans = ""
        while len(characters) > 0 and len(digits) > 0:
            ans += characters.pop()
            ans += digits.pop()
        if len(characters) == 0 and len(digits) == 0:
            return ans
        if len(characters) == 1:
            return ans + characters.pop()
        if len(digits) == 1:
            return digits.pop() + ans
        if len(characters) > 1 or len(digits) > 1:
            return ""
        