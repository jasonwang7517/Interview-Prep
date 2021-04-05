class Solution(object):
    def fairCandySwap(self, A, B):
        diff = (sum(A) - sum(B)) // 2
        bSet = set(B)
        for i in A:
            if (i - diff) in bSet:
                ans = [i, i - diff]
                return ans