"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

class ValidPalindromeII(object):
    def validPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                new_string_1 = s[: i] + s[i + 1 :]
                new_string_2 = s[: len(s) - i - 1] + s[len(s) - i:]
                return self.isPalindrome(new_string_1) or self.isPalindrome(new_string_2)
        return True
        
    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
        