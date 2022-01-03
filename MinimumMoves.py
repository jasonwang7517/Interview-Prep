"""
You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.
"""

class MinimumMoves(object):
    def minimumMoves(self, s):
        ans = 0
        index = 0
        while index < len(s):
            if s[index] == 'X':
                ans += 1
                index += 3
            else:
                index += 1
        return ans
        
        