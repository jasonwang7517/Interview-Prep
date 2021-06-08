class Solution(object):
    def countGoodSubstrings(self, s):
        ans = 0
        for i in range(0, len(s) - 2):
            currStr = set(s[i:i + 3])
            if len(currStr) == 3:
                ans += 1
        return ans
