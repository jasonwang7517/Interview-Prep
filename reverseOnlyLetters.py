"""
Given a string s, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
"""

class ReverseOnlyLetters(object):
    def reverseOnlyLetters(self, S):
        letters = []
        otherChars = [0] * 100
        for i in range(0, len(S)):
            curr = S[i]
            if (ord(curr) >= 65 and ord(curr) <= 90) or (ord(curr) >= 97 and ord(curr) <= 122):
                letters.append(curr)
            else:
                otherChars[i] = curr
        index = 0
        ans = ""
        while index < len(S):
            if otherChars[index] != 0:
                ans += otherChars[index]
            else:
                ans += letters.pop()
            index += 1
        return ans