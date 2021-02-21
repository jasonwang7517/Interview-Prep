class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split(" ")
        for i in range(0, len(words)):
            length = len(searchWord)
            if len(words[i]) >= length:
                currWord = words[i]
                if currWord[0:length] == searchWord:
                    return i + 1
        return -1
