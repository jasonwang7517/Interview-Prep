class Solution(object):
    def minOperations(self, s):
        oddAns = 0
        evenAns = 0
        for i in range(0, len(s)):
            if i % 2 == int(s[i]):
                oddAns += 1
            else:
                evenAns += 1
        return min(oddAns, evenAns)
