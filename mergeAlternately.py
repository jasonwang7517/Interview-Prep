class Solution(object):
    def mergeAlternately(self, word1, word2):
        word1Index = 0
        word2Index = 0
        ans = ""
        while word1Index < len(word1) and word2Index < len(word2):
            ans += word1[word1Index]
            ans += word2[word2Index]
            word1Index += 1
            word2Index += 1
        if word1Index >= len(word1) and word2Index < len(word2):
            ans += word2[word2Index:]
        elif word2Index >= len(word2) and word1Index < len(word1):
            ans += word1[word1Index:]
        return ans