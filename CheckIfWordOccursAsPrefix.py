"""
Given a sentence that consists of some words separated by a single space, and a searchWord.

You have to check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).

If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string S is any leading contiguous substring of S.
"""

class CheckIfWordOccursAsPrefix(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split(" ")
        for i in range(0, len(words)):
            length = len(searchWord)
            if len(words[i]) >= length:
                currWord = words[i]
                if currWord[0:length] == searchWord:
                    return i + 1
        return -1
