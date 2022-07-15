"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). 

If the character ch does not exist in word, do nothing.
    - For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.
"""

class ReversePrefixOfWord(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        index_of_ch = word.index(ch)
        to_reverse = word[:index_of_ch + 1]
        to_keep = word[index_of_ch + 1:]
        to_reverse = to_reverse[::-1]
        return to_reverse + to_keep