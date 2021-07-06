"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.
"""

class RedistributeCharactersToMakeAllStringsEqual(object):
    def makeEqual(self, words):
        letters = {}
        for i in words:
            for j in i:
                if j in letters:
                    letters[j] += 1
                else:
                    letters[j] = 1
        for i in letters:
            if letters[i] % len(words) != 0:
                return False
        return True
        