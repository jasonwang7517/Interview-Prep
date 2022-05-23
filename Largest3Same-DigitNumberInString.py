"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:
    - It is a substring of num with length 3.
    - It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:
    - A substring is a contiguous sequence of characters within a string.
    - There may be leading zeroes in num or a good integer.
"""

class Largest3SameDigitNumberInString(object):
    def largestGoodInteger(self, num):
        index = 3
        ans = ""
        while index <= len(num):
            window = num[index - 3:index]
            if window[0] == window[1] and window[1] == window[2]:
                st = ''.join(window)
                ans = max(ans, st)
            index += 1
        return ans