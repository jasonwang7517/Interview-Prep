"""
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
"""

class FirstPalindromicStringInArray(object):
    def firstPalindrome(self, words):
        for i in words:
            if self.isPalindrome(i):
                return i
        return ""
        
    def isPalindrome(self, word):
        length = len(word)
        for i in range(0, len(word) // 2):
            if word[i] != word[length - i - 1]:
                return False
        return True