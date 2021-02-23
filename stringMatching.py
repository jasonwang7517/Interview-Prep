class Solution(object):
    def stringMatching(self, words):
        ans = set()
        for i in range(0, len(words) - 1):

            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    ans.add(words[i])
                elif words[j] in words[i]:
                    ans.add(words[j])
        return list(ans)
