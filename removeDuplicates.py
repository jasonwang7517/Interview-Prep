class Solution(object):
    def removeDuplicates(self, S):
        index = 0
        while index < len(S) - 1:
            if S[index] == S[index + 1]:
                if index < len(S) - 2:
                    S = S[0: index] + S[index + 2::]
                else:
                    S = S[0: index]
                index = max(0, index - 1)
            else:
                index += 1 
        return S