"""
You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, 
and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.
"""

class Solution(object):
    def countAsterisks(self, s):
        checking = True
        ans = 0
        for i in s:
            if checking and i == '|':
                checking = False
            elif not checking and i == '|':
                checking = True
            elif checking and i == '*':
                ans += 1
        return ans