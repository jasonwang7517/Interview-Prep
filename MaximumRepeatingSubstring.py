"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is 
k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.
"""

class MaximumRepeatingSubstring(object):
    def maxRepeating(self, sequence, word):
        ans = 0
        current_sub = word
        while current_sub in sequence:
            ans += 1
            current_sub += word
        return ans
        