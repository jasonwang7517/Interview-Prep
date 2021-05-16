class Solution(object):
    def sortSentence(self, s):
        words = s.split(" ")
        sentence = [0] * len(words)
        for w in words:
            index = int(w[-1]) - 1
            sentence[index] = w[:-1]
        ans = ""
        for i in sentence:
            ans += i + " "
        return ans[:-1]