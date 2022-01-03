"""
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.
"""

class CheckIfAllAsBeforeBs(object):
    def checkString(self, s):
        b_flag = False
        for i in s:
            if i == 'b':
                b_flag = True
            elif i == 'a' and b_flag:
                return False
        return True