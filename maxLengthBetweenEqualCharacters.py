class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        ans = -1
        seen = {}
        for i in range(0, len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
            else:
                ans = max(ans, i - seen[s[i]] - 1)
        return ans