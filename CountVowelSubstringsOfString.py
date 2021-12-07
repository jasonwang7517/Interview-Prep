"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.
"""

class Solution(object):
    def countVowelSubstrings(self, word):
        length = 5
        ans = 0
        while length <= len(word):
            for i in range(0, len(word) - length + 1):
                currWord = word[i : i + length]
                if 'a' in currWord and 'e' in currWord and 'i' in currWord and 'o' in currWord and 'u' in currWord and self.onlyVowels(currWord):
                    ans += 1
            length += 1
        return ans
    
    def onlyVowels(self, word):
        for i in word:
            if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
                return False
        return True
        