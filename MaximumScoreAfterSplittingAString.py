"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
"""

class MaximumScoreAfterSplittingAString(object):
    def maxScore(self, s):
        num1s = 0
        for i in s:
            if i == '1':
                num1s += 1
        num0s = 0
        ans = 0
        for i in range(0, len(s) - 1):
            if s[i] == '0':
                num0s += 1
            elif s[i] == '1':
                num1s -= 1
            if num0s + num1s > ans:
                ans = num0s + num1s
        return ans
        