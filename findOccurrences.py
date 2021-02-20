class Solution(object):
    def findOcurrences(self, text, first, second):
        words = text.split(" ")
        ans = []
        for i in range(0, len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])
                i += 2
        return ans
