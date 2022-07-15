"""
Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 
is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.
"""

class CheckWhetherTwoStringsAreAlmostEqual(object):
    def checkAlmostEquivalent(self, word1, word2):
        letters = {}
        letters2 = {}
        for i in word1:
            if i not in letters:
                letters[i] = 1
            else:
                letters[i] += 1
        for i in word2:
            if i not in letters2:
                letters2[i] = 1
            else:
                letters2[i] += 1
        for i in letters:
            if i not in letters2:
                if letters[i] > 3:
                    return False
            else:
                total_mistakes = abs(letters[i] - letters2[i])
                if total_mistakes > 3:
                    return False
        for i in letters2:
            if i not in letters:
                if letters2[i] > 3:
                    return False
        return True
        