"""
    Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

    In the American keyboard:

    - the first row consists of the characters "qwertyuiop",
    - the second row consists of the characters "asdfghjkl", and
    - the third row consists of the characters "zxcvbnm".
"""
class KeyboardRow(object):
    def findWords(self, words):
        firstRow = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        secondRow = {'a', 's', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l'}
        thirdRow = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        ans = []

        for word in words:
            first = word[0].lower()
            toAdd = True
            if first in firstRow:
                for i in range(1, len(word)):
                    if word[i].lower() not in firstRow:
                        toAdd = False
                        break
                if toAdd:
                    ans.append(word)
            elif first in secondRow:
                for i in range(1, len(word)):
                    if word[i].lower() not in secondRow:
                        toAdd = False
                        break
                if toAdd:
                    ans.append(word)
            else:
                for i in range(1, len(word)):
                    if word[i].lower() not in thirdRow:
                        toAdd = False
                        break
                if toAdd:
                    ans.append(word)
        return ans