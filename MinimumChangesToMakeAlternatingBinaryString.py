"""
    You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

    The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

    Return the minimum number of operations needed to make s alternating.
"""

class MinimumChangesToMakeAlternatingBinaryString(object):
    def minOperations(self, s):
        oddAns = 0
        evenAns = 0
        for i in range(0, len(s)):
            if i % 2 == int(s[i]):
                oddAns += 1
            else:
                evenAns += 1
        return min(oddAns, evenAns)
