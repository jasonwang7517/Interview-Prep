"""
You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the 
capitalization of each word such that:

    If the length of the word is 1 or 2 letters, change all letters to lowercase.
    Otherwise, change the first letter to uppercase and the remaining letters to lowercase.

Return the capitalized title.
"""

class CapitalizeTheTitle(object):
    def capitalizeTitle(self, title):
        words = title.split()
        for i in range(len(words)):
            current_word = words[i]
            if len(current_word) <= 2:
                words[i] = current_word.lower()
            else:
                word = words[i].lower()
                first_index = ord(word[0])
                first_char = chr(first_index - 32)
                new_word = first_char + word[1:]
                words[i] = new_word
        ans = ""
        for i in words:
            ans += i + ' '
        return ans[:-1]     

