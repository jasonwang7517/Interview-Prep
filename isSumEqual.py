class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        word1 = ""
        for i in firstWord:
            word1 += str(ord(i) - ord('a'))
        word2 = ""
        for i in secondWord:
            word2 += str(ord(i) - ord('a'))
        target = ""
        for i in targetWord:
            target += str(ord(i) - ord('a'))

        return (int(word1) + int(word2)) == int(target)
