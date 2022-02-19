"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
"""

class VerifyingAnAlienDictionary(object):
    def isAlienSorted(self, words, order):
        letters = {}
        for i in range(len(order)):
            letters[order[i]] = i
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            for j in range(len(current_word)):
                if j >= len(next_word) or letters[current_word[j]] > letters[next_word[j]]:
                    return False
                if letters[current_word[j]] < letters[next_word[j]]:
                    break
        return True
            
            
        