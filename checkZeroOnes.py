class Solution(object):
    def checkZeroOnes(self, s):
        longest1s = 0
        curr1s = 0
        longest0s = 0
        curr0s = 0
        for i in s:
            if i == '0':
                if curr1s == 0:
                    curr0s += 1
                elif curr1s > 0:
                    longest1s = max(longest1s, curr1s)
                    curr1s = 0
                    curr0s = 1
            elif i == '1':
                if curr0s == 0:
                    curr1s += 1
                elif curr0s > 0:
                    longest0s = max(longest0s, curr0s)
                    curr0s = 0
                    curr1s = 1
        longest1s = max(longest1s, curr1s)
        longest0s = max(longest0s, curr0s)
        return longest1s > longest0s
