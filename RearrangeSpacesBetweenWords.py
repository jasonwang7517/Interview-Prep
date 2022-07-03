"""
You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's 
guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place 
the extra spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.
"""

class RearrangeSpacesBetweenWords(object):
    def reorderSpaces(self, text):
        ans = []
        spaces = 0
        for i in text:
            if i == ' ':
                spaces += 1
        words = text.split()
        if len(words) == 1:
            ans.append(words[0])
            ans.append(' ' * spaces)
            return ''.join(ans)
        spaces_per_word = spaces // (len(words) - 1)
        remainder = spaces % (len(words) - 1)
        for i in words:
            ans.append(i)
            ans.append(' ' * spaces_per_word)
        ans.pop()
        ans.append(' ' * remainder)
        return ''.join(ans)
        