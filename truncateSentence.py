class Solution(object):
    def truncateSentence(self, s, k):
        words = s.split(" ")
        return ' '.join(words[:k])
