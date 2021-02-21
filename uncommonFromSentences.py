class Solution(object):
    def uncommonFromSentences(self, A, B):
        dict ={}
        ans = []
        for s in A.split(" "):
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] = dict[s] + 1
        for s in B.split(" "):
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] = dict[s] + 1
        for s in dict:
            if dict[s] == 1:
                ans.append(s)
        return ans