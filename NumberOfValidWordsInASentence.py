"""
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. 
Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:
    - It only contains lowercase letters, hyphens, and/or punctuation (no digits).
    - There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
    - There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).

Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.
"""

class Solution(object):
    def countValidWords(self, sentence):
        ans = 0
        punctuation = {'!', '.', ','}
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        words = sentence.split()
        for word in words:
            hyphens = 0
            index = 0
            to_add = True
            while index < len(word):
                if (word[index] in punctuation and index != len(word) - 1) or (word[index] in digits) or (word[index] == '-' and (index == 0 or index == len(word) - 1)):
                    to_add = False
                    break
                elif word[index] == '-' and word[index - 1].isalpha() and word[index + 1].isalpha():
                    hyphens += 1
                    if hyphens > 1:
                        to_add = False
                        break
                elif word[index] == '-':
                    to_add = False
                    break
                index += 1
            if to_add:
                ans += 1
        return ans
                